from calendar import timegm
from datetime import timedelta, datetime, timezone
from fastapi import Request, Depends
from utils.exceptions import ServiceException
from typing import Union
from fastapi.security import HTTPBearer
from pydantic import ValidationError
import jwt
from utils.config import SECRET_KEY

SECURITY_ALGORITHM = 'HS256'
DEFAULT_EXPIRY = timedelta(hours=10)

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


class Authorizer:
    def __init__(self, uid: str, sub: str, roles: list[str]):
        self.uid = uid
        self.sub = sub
        self.roles = roles

    def to_dict(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('uid'), data.get('sub'), data.get('role'))


def generate_token(auth: Authorizer, expires_delta: Union[timedelta, None] = DEFAULT_EXPIRY) -> str:
    to_encode = auth.to_dict()
    to_encode.update({"exp": datetime.now(tz=timezone.utc) + expires_delta})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt


def is_exp(token):
    now = timegm(datetime.now(tz=timezone.utc).utctimetuple())
    return now > token['exp']


def validate_token(request: Request, auth_credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token to get user info
    """
    try:
        print(auth_credentials)
        leetime = 600
        payload = jwt.decode(auth_credentials.credentials, SECRET_KEY, leeway=timedelta(seconds=leetime),
                             algorithms=[SECURITY_ALGORITHM])
        if is_exp(payload):
            # In lee time we throw
            raise ServiceException(
                code=5,
                detail="Refresh token"
            )
            # throw message refresh token

        request.state.user = Authorizer.from_dict(payload)
        return request.state.user
    except (jwt.PyJWTError, ValidationError) as ex:
        print(ex)
        raise ServiceException(
            code=6,
            detail="Could not validate credentials"
        )
