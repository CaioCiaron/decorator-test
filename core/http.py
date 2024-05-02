from typing import TypedDict, TypeVar, Generic
T = TypeVar('T')

class HttpEvent(TypedDict, Generic[T]):
  httpMethod: str
  payload: T
  resource: str