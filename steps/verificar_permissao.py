from behave import given, when, then
from index import *

@given("verificar permissao")
def given_carregar_arquivo_configuracao(context):
    context.configuracao = carregar_arquivos()    
    assert context.configuracao != None

@when("a foto {foto} do personagem visitante for capturada")
def when_simular_escolha_foto(context, foto):
    context.foto_escolhida = simular_escolha_personagem(foto)
    
    assert context.foto_escolhida != None

@then("o personagem {foto_personagem_simulado} deve ser reconhecido")
def then_personagem_reconhecido(context, foto_personagem_simulado):
    context.reconhecido, context.mensagem, context.dados = reconhecer_personagem(foto_personagem_simulado)
    
    assert context.reconhecido == True

@when("verificar permissao do {dados_personagem_identificado}")
def when_verificar_permissao_personagem(context, dados_personagem_identificado):
    context.reconhecido, context.mensagem, context.dados = reconhecer_personagem(dados_personagem_identificado)
    
    assert context.dados['permissao'] != None

@then("permitir a entrada do personagem em Zion")
def then_permitir_entrada_em_zion(context):
    context.permitido = verificar_permissao_zion(context.reconhecido, context.mensagem, context.dados)
    
    assert context.permitido == True

@then("não permitir a entrada do personagem em Zion")
def then_nao_permitir_entrada_em_zion(context):
    context.negado = verificar_permissao_zion(context.reconhecido, context.mensagem, context.dados)
    
    assert context.negado == True
    
