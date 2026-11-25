# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-24
# Nome: Desafio 03
# 
"""
Neste desafio você aprenderá a construir fluxos compostos por múltiplas etapas utilizando LangChain.

O objetivo é compreender como dividir um problema em partes menores e encadear o processamento da informação.

Ao final deste desafio você deverá ser capaz de:

- Criar múltiplos PromptTemplates
- Encadear etapas de processamento
- Utilizar a saída de uma etapa como entrada da próxima
- Construir pipelines reutilizáveis
- Compreender a base conceitual para agentes futuros
"""

# Imports
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Carregar o ambiente
load_dotenv(".env")

# ---------------------------------------------------------------
# ETAPA 0: criar o modelo de chat que será usado em todas as etapas
# ---------------------------------------------------------------
llm = init_chat_model(api_key=os.environ.get("OPENAI_API_KEY"), model= "gpt-4.1")

# ---------------------------------------------------------------
# ETAPA 1: prompt de RESUMO
# O {texto} entre chaves é um espaço que será preenchido depois
# ---------------------------------------------------------------
prompt_resumo = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente. Resuma o texto do usuário de forma concisa."),
    ("user", "{texto}"),
])

# ---------------------------------------------------------------
# ETAPA 2: prompt de ANÁLISE
# Recebe o RESUMO produzido na etapa 1 (variável {resumo})
# ---------------------------------------------------------------
prompt_analise = ChatPromptTemplate.from_messages([
    ("system", "Analise o impacto: pontos fortes, riscos e oportunidades."),
    ("user", "Resumo:\n{resumo}"),
])

# ---------------------------------------------------------------
# ETAPA 3: prompt de RELATÓRIO
# Recebe a ANÁLISE (etapa 2)
# ---------------------------------------------------------------
prompt_relatorio = ChatPromptTemplate.from_messages([
    ("system", "Construa um relatório executivo com no máximo 10 linhas"),
    ("user", "Análise:\n{analise}"),
])


# ---------------------------------------------------------------
# Cada função abaixo executa UMA cadeia "prompt | modelo":
# o prompt é formatado com os valores, enviado ao modelo,
# e .content devolve a resposta em texto puro.
# ---------------------------------------------------------------
def fazer_resumo(texto_do_usuario: str) -> str:
    cadeia = prompt_resumo | llm
    resposta = cadeia.invoke({"texto": texto_do_usuario})
    return resposta.content


def fazer_analise(resumo: str) -> str:
    cadeia = prompt_analise | llm
    resposta = cadeia.invoke({"resumo": resumo})
    return resposta.content


def fazer_relatorio(analise: str) -> str:
    cadeia = prompt_relatorio | llm
    resposta = cadeia.invoke({"analise": analise})
    return resposta.content


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL: executa as etapas EM ORDEM,
# passando a saída de uma como entrada da seguinte
# ---------------------------------------------------------------
if __name__ == "__main__":
    texto_do_usuario = input("Entre com a informação a ser analisada:")

    print("Etapa 1: gerando o resumo...")
    resumo = fazer_resumo(texto_do_usuario)
    print(resumo, "\n")

    print("Etapa 2: gerando a análise...")
    analise = fazer_analise(resumo)
    print(analise, "\n")

    print("Etapa 3: montando o relatório executivo...")
    relatorio = fazer_relatorio(analise)
    print(relatorio)