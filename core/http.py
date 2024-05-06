from typing import Any, TypedDict, TypeVar, Generic
from enum import Enum

T = TypeVar('T')

class HttpEvent(TypedDict, Generic[T]):
  httpMethod: str
  payload: T
  resource: str
  roles: list[str]


class HttpResponse(TypedDict, Generic[T]):
  statusCode: int
  message: Any
  body: T


class Method(Enum):
  GET = 'GET'
  POST = 'POST'
  PUT = 'PUT'
