class ERROR_CODE:
    # Admin
    SUCCESS: int = 0
    SERVER_ERROR: int = 1
    WRONG_DATA_FORMAT: int = 2
    TOKEN_EXPIRE: int = 3
    TOKEN_REFRESH: int = 4
    TOKEN_INVALID: int = 5
    ADMIN_INVALID_EMAIL: int = 9
    ADMIN_EXISTS_EMAIL = 10
    ADMIN_NOT_EXIST = 11
    EMAIL_ERROR: int = 17
    PASSWORD_ERROR: int = 16
    LIST_ERROR: int = 12
    NAME_ERROR: int = 13
    ROLE_ID_ERROR: int = 14
    FLAG_ERROR: int = 15
    REQUIRE_RE_LOGIN_SYSTEM = 101 # Error refesh token expire time - re-login
    SUPPER_ADMIN_ERROR: int = 18
    ROLE_EXISTS_NAME: int = 19
    ROLE_NOT_EXIST = 20

    PERMISSION_EXISTS_NAME: int = 21
    PERMISSION_NOT_EXIST = 22
    PERMISSION_EXISTS_CODE: int = 23
    PERMISSION_PARENT_NOT_EXIST: int = 24
    PERMISSION_ERROR: int = 25

    # User error code
    USER_NOT_EXIST: int = 201
