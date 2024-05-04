from typing import Any, TypedDict, TypeVar, Generic
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