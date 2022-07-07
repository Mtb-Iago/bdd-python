from behave import given, when, then
from index import *

@given("carregar arquivos de configuracao")
def given_carregar_arquivo_configuracao(context):
    context.configuracao = carregar_arquivos()    
    assert context.configuracao != None
