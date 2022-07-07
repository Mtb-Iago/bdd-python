from behave import given, when, then
from index import *

@given("reconhecer personagem")
def given_carregar_arquivo_configuracao(context):
    context.configuracao = carregar_arquivos()    
    assert context.configuracao != None

@when("a foto {foto} de um personagem visitante for capturada")
def when_simular_escolha_foto(context, foto):
    context.foto_escolhida = simular_escolha_personagem(foto)
    
    assert context.foto_escolhida != None

@then("o personagem {foto_personagem_simulado} deve ser reconhecido para prosseguir")
def then_personagem_reconhecido(context, foto_personagem_simulado):
    context.reconhecido, context.mensagem, context.dados = reconhecer_personagem(foto_personagem_simulado)
    
    assert context.reconhecido == True