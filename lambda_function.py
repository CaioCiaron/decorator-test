from core.http import HttpEvent
from web import Router

def lambda_handler(event: HttpEvent):
  router = Router()
  return router.resolve(event)

print(
  lambda_handler(
    {
      'httpMethod': 'GET', 
      'resource': '/pessoas/{id_pessoa}', 
      'payload': {'nome': 'Pessoa 1', 'descricao': 'Primeira Pessoa'}
    }
  )
)