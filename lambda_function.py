from core.http import HttpEvent
from web import Router
from paste import httpserver

def lambda_handler(event: HttpEvent):
  router = Router()
  return router.resolve(event)

print(
  lambda_handler(
    {
      'httpMethod': 'POST', 
      'resource': '/pessoas', 
      'payload': {'nome': 'Pessoa 1', 'descricao': 'Primeira Pessoa'},
      'roles': []
    }
  )
)
