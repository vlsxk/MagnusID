from enum import Enum


class AppRoute(str, Enum):

    AUTH = "/front/login"
    ORG_STRUCTURE = "/company-structure"
    PROFILE="/profile"
