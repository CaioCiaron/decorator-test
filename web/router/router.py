from core import Singleton, Method, RequestConfig
from core.http import HttpEvent


class Router(RequestConfig, metaclass=Singleton):
  
  def resolve(self, event: HttpEvent):
    try:
      httpMethod = event['httpMethod'].upper()
      apiGatewayResource = event['resource']
      return self._mappings[Method(httpMethod)][apiGatewayResource](event)
    except Exception as e:
      print('The requested URL is not registered for this method')
    

router_instance = Router()