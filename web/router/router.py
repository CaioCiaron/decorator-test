from core import Singleton, RequestConfig
from core.http import HttpEvent, Method
from core.request_config import EndpointData


class Router(RequestConfig, metaclass=Singleton):
  
  def resolve(self, event: HttpEvent):
    try:
      httpMethod = event['httpMethod'].upper()
      apiGatewayResource = event['resource']
      apiMapping = self._mappings[Method(httpMethod)][apiGatewayResource]
    except Exception as e:
      print('The requested URL is not registered for this method')
    
    if not self._resolveRoles(event, apiMapping):
      return {'statusCode': 401, 'body': 'Você não possui permissão para a acessar este recurso.'}
    
    return apiMapping['handler'](event)
    
  def _resolveRoles(self, event: HttpEvent, endpointData: EndpointData) -> bool:
    if not endpointData['roles']: return True
    
    for role in event['roles']:
      if role in endpointData['roles']:
        return True
    
    return False

router_instance = Router()