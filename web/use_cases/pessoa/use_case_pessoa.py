from core.http import HttpEvent
from web import Router
from .pessoa import Pessoa


pessoas: dict[int, Pessoa] = {}

@Router.Get('/pessoas/{id_pessoa}')
def get_pessoas(event: HttpEvent):
  return event

@Router.Post('/pessoas')
def post_pessoas(event: HttpEvent[Pessoa]):
  pessoas[1] = event['payload']
  return pessoas[1]


