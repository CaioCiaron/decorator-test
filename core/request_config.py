from typing import Callable
from core.http import HttpEvent, HttpResponse, Method
from typing import TypedDict

_EndpointHandler = Callable[[HttpEvent], HttpResponse]
_EndpointDecorator = Callable[[_EndpointHandler], _EndpointHandler]

class EndpointData(TypedDict):
  handler: _EndpointHandler
  roles: list[str]

class RequestConfig:
  _mappings: dict[Method, dict[str, EndpointData]] = {
    Method.GET: {},
    Method.POST: {},
    Method.PUT: {}
    }

  @classmethod
  def Get(cls, url: str, roles: list[str] = []) -> _EndpointDecorator:
    return cls._register_method(Method.GET, url, roles)

  @classmethod
  def Post(cls, url: str, roles: list[str] = []) -> _EndpointDecorator:
    return cls._register_method(Method.POST, url, roles)
  
  @classmethod
  def Put(cls, url: str, roles: list[str] = []) -> _EndpointDecorator:
    return cls._register_method(Method.PUT, url, roles)
  
  @classmethod
  def _register_method(cls, http_method: Method, url: str, roles: list[str] = []) -> _EndpointDecorator:
    return lambda func: cls._decorator_wrapper(http_method, url, func, roles)

  @classmethod
  def _decorator_wrapper(
    cls,
    http_method: Method,
    url: str,
    func: _EndpointHandler,
    roles: list[str] = []
    ) -> _EndpointHandler:
    print(f'Registering {http_method} for URL {url}')
    if url not in cls._mappings[Method(http_method)]:
      cls._mappings[Method(http_method)][url] = {'handler': func, 'roles': roles}
    return func
  
  