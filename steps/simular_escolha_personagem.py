from behave import given, when, then
from index import *

@given("simula um personagem para entrar em Zion")
def given_carregar_arquivo_configuracao(context):
    context.configuracao = carregar_arquivos()    
    assert context.configuracao != None

@when("o personagem {foto} foi selecionado")
def when_simular_escolha_foto(context, foto):
    context.foto_escolhida = simular_escolha_personagem(foto)
    
    assert context.foto_escolhida != None