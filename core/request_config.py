from core.method import Method


class RequestConfig:
  _mappings = {
    Method.GET: {},
    Method.POST: {},
    Method.PUT: {}
    }

  @classmethod
  def Get(cls, url: str):
    def decorator_wrapper(func):
      print(f'Registering GET method for URL {url}')
      if url not in cls._mappings[Method.GET]:
        cls._mappings[Method.GET][url] = func
      return func
    return decorator_wrapper

  @classmethod
  def Post(cls, url: str):
    def decorator_wrapper(func):
      print(f'Registering POST method for URL {url}')
      if url not in cls._mappings[Method.POST]:
        cls._mappings[Method.POST][url] = func
      return func
    return decorator_wrapper
  
  @classmethod
  def Put(cls, url: str):
    def decorator_wrapper(func):
      print(f'Registering PUT method for URL {url}')
      if url not in cls._mappings[Method.PUT]:
        cls._mappings[Method.PUT][url] = func
      return func
    return decorator_wrapper