# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-23
# Nome: Desafio 02
# 
# Neste desafio você fará a transição da chamada direta para a API da LLM para o ecossistema LangChain.

"""
O objetivo não é criar um agente ainda.

O objetivo é entender os componentes fundamentais que servirão de base para toda a arquitetura que construiremos posteriormente.

Ao final deste desafio você deverá ser capaz de:

 - Instalar e configurar o LangChain
- Utilizar Chat Models
- Utilizar PromptTemplate
- Utilizar Runnable
- Separar prompt de execução
- Criar uma aplicação mais estruturada do que a do Desafio 01
"""

# Imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Carregar o ambiente
load_dotenv(".env")

pergunta = "Qual a diferença entre transporte aéreo e marítimo?"

# criar o modelo
llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model= "gpt-4.1" ) #model="gpt-5.5")

# criar o prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em logística. Responda de forma clara e direta."),
    ("human", "Responda a pergunta abaixo: \nPergunta: {topico}")
])

# executar a chain
chain = prompt | llm

# exibir o resultado

def faz_pergunta(chain, pergunta):
    
    resposta = chain.invoke({
        "topico": pergunta
    })

    print("Provider: OpenAI")
    print("Modelo: gpt-4.1")
    print("Pergunta:")
    print(pergunta)
    print("Resposta:")
    print(resposta.content)

faz_pergunta(chain, pergunta)

pergunta = input("Entre com a sua pergunta:")

faz_pergunta(chain, pergunta)
