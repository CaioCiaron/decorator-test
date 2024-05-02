from typing import Callable
from core.method import Method


class RequestConfig:
  _mappings = {
    Method.GET: {},
    Method.POST: {},
    Method.PUT: {}
    }

  @classmethod
  def Get(cls, url: str):
    return cls._decorator_wrapper(Method.GET, url)

  @classmethod
  def Post(cls, url: str):
    return cls._decorator_wrapper(Method.POST, url)
  
  @classmethod
  def Put(cls, url: str):
    return cls._decorator_wrapper(Method.PUT, url)
  
  @classmethod
  def _decorator_wrapper(cls, http_method: Method, url: str):
    return lambda func: cls._register_method(http_method, url, func)

  @classmethod
  def _register_method(cls, http_method: Method, url: str, func: Callable):
    print(f'Registering {http_method} for URL {url}')
    if url not in cls._mappings[Method(http_method)]:
      cls._mappings[Method(http_method)][url] = func
    return func
  
  