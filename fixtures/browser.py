import re
import uuid
from pages.authentication_page import AuthenticationPage
import allure
import pytest
from playwright.sync_api import Playwright, Page, expect
from tools.routes import AppRoute
from config import Settings
from pathlib import Path
import json
from datetime import datetime, timedelta

@pytest.fixture(scope="session", autouse=True)
def playwright_global_settings(playwright: Playwright, settings: Settings):
    expect.set_options(timeout=settings.expect_timeout)
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="session")
def admin_auth_token(playwright: Playwright, settings: Settings) -> str:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=f"{settings.app_url}/")
    page = context.new_page()

    authentication_page = AuthenticationPage(page)
    authentication_page.visit(AppRoute.AUTH)

    authentication_page.authentication_form.check_visible()

    authentication_page.authentication_form.fill(
        username=settings.admin_username,
        password=settings.admin_password
    )
    authentication_page.click_authentication_button()
    authentication_page.check_current_url(re.compile(".*/profile"))
    token = page.evaluate("localStorage.getItem('token')")
    browser.close()
    return token

@pytest.fixture
def unauthorized_page(playwright: Playwright, settings: Settings) -> Page:

    expect.set_options(timeout=settings.expect_timeout)
    playwright.selectors.set_test_id_attribute("data-test")

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=f"{settings.app_url}/",
        record_video_dir=settings.videos_dir
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)


    page = context.new_page()

    yield page

    tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
    context.tracing.stop(path=tracing_file)
    browser.close()

    allure.attach.file(tracing_file, name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


STALE_AFTER = timedelta(minutes=18)   # чуть меньше TTL токена (20 мин), с запасом
STORAGE_STATE_FILE = Path("auth_state.json")


def _state_is_fresh(storage_state_file: Path) -> bool:
    """True, если файл состояния существует и моложе STALE_AFTER."""
    if not storage_state_file.exists():
        return False
    age = datetime.now() - datetime.fromtimestamp(storage_state_file.stat().st_mtime)
    return age < STALE_AFTER


def _token_from_file(storage_state_file: Path) -> str:
    """Достаёт токен из сохранённого storage_state."""
    try:
        state = json.loads(storage_state_file.read_text(encoding="utf-8"))
        for origin in state.get("origins", []):
            for item in origin.get("localStorage", []):
                if item.get("name") == "token":
                    return item.get("value", "")
    except (json.JSONDecodeError, OSError):
        return ""
    return ""

def _token_is_valid(playwright: Playwright, settings: Settings, token: str) -> bool:
    """Проверяет живость токена лёгким запросом к авторизованному эндпоинту."""
    if not token:
        return False
    try:
        response = playwright.request.get(
            f"{settings.app_url}/profile",   # ← подставь свой дешёвый auth-эндпоинт
            headers={"Authorization": f"Bearer {token}"},
        )
        return response.ok
    except Exception:
        return False

@pytest.fixture(scope="module")
def authorized_admin_page(playwright: Playwright,
                          settings: Settings,
                          admin_auth_token :str) -> Page:



        # expect.set_options(timeout=settings.expect_timeout)
        # playwright.selectors.set_test_id_attribute("data-test")


        # storage_state_file = Path("auth_state.json")

        context_args = {
            "base_url": f"{settings.app_url}/",
            "record_video_dir": settings.videos_dir,
        }

        use_cached_state = (
                _state_is_fresh(STORAGE_STATE_FILE)
                and _token_is_valid(playwright, settings, _token_from_file(STORAGE_STATE_FILE))
        )

        browser = playwright.chromium.launch(headless=settings.headless)

        if use_cached_state:
            # --- Ветка 1: сессия сохранена — подгружаем её ---
            context_args["storage_state"] = str(STORAGE_STATE_FILE)
            context = browser.new_context(**context_args)
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
        else:
            # --- Ветка 2: файла нет, он протух или токен мёртв — логинимся заново ---
            if STORAGE_STATE_FILE.exists():
                STORAGE_STATE_FILE.unlink()  # убираем битый кэш, чтобы не мешал другим


            context = browser.new_context(**context_args)
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            # add_init_script срабатывает ДО загрузки страницы:
            # приложение стартует уже с токеном в localStorage
            context.add_init_script(
                f"window.localStorage.setItem('token', {json.dumps(admin_auth_token)});"
            )
            page = context.new_page()
            page.goto("/")
            expect(page.locator(".profile__header.text-h3")).to_be_visible()
            # Сохраняем куки + localStorage на диск для следующих тестов
            context.storage_state(path=str(STORAGE_STATE_FILE))

        yield page


        tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
        context.tracing.stop(path=tracing_file)

        video_path = page.video.path()

        # Обновляем кэш свежим состоянием: токен здесь уже отрефрешен приложением
        try:
            expect(page.locator(".profile__header.text-h3")).to_be_visible(timeout=3_000)
            context.storage_state(path=str(STORAGE_STATE_FILE))
        except AssertionError:
            # страница разлогинена или в странном состоянии — битый кэш не сохраняем
            if STORAGE_STATE_FILE.exists():
                STORAGE_STATE_FILE.unlink()

        context.close()
        browser.close()

        allure.attach.file(tracing_file, name='trace', extension='zip')
        allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)


