from core.http import HttpEvent, HttpResponse
from web import Router
from .pessoa import Pessoa


pessoas: dict[int, Pessoa] = {}

@Router.Get('/pessoas/{id_pessoa}')
def get_pessoas(event: HttpEvent) -> HttpResponse[list[Pessoa]]:
  return {
    'statusCode': 200,
    'message': 'success',
    'body': [{'nome': 'pessoa 1', 'descricao': 'pessoa 1'}]
  }

@Router.Post('/pessoas', roles=['admin'])
def post_pessoas(event: HttpEvent[Pessoa]) -> HttpResponse[Pessoa]:
  pessoas[1] = event['payload']
  return {
    'statusCode': 201,
    'message': 'Pessoa criada com sucesso!',
    'body': {'nome': 'pessoa 2', 'descricao': 'pessoa 2'}
  }


