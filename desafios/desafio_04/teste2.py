# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-25
# Nome: Desafio 04
# 
"""
Neste desafio você aprenderá a fornecer capacidades externas para uma LLM.

Até agora o modelo apenas respondeu perguntas.

A partir deste desafio ele poderá executar ações através de ferramentas.

O Que Vamos Construir:

Um assistente capaz de:

- Somar
- Subtrair
- Multiplicar
- Dividir

Utilizando ferramentas registradas no LangChain.
"""

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

# ---------------------------------------------------------------
# Ler as variaveis de ambiente
# ---------------------------------------------------------------
load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ---------------------------------------------------------------
# ETAPA 1: criar uma ferramenta que soma
# ---------------------------------------------------------------
@tool
def somar(a: float, b: float) -> float:
    """Soma dois números.

    Args:
        a: Primeiro número
        b: Segundo número
    """
    return a + b

# ---------------------------------------------------------------
# ETAPA 2: criar uma ferramenta que subtrai
# ---------------------------------------------------------------
@tool
def subtrair(a: float, b: float) -> float:
    """Subtrai o segundo número do primeiro.

    Args:
        a: Número do qual subtrair
        b: Número a subtrair
    """
    return a - b

# ---------------------------------------------------------------
# ETAPA 3: criar uma ferramenta que multiplica
# ---------------------------------------------------------------
@tool
def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números.

    Args:
        a: Primeiro número
        b: Segundo número
    """
    return a * b

# ---------------------------------------------------------------
# ETAPA 4: criar uma ferramenta que divide
# ---------------------------------------------------------------
@tool
def dividir(a: float, b: float) -> str:
    """Divide o primeiro número pelo segundo.

    Args:
        a: Numerador
        b: Denominador (não pode ser zero)
    """
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return str(a / b)

# ---------------------------------------------------------------
# ETAPA extra: criar uma ferramenta que informe a data do sistema
# ---------------------------------------------------------------
from datetime import datetime
@tool
def data_hora_atual() -> str:
    """Obtem a data e hora do sistema

    Args:
        None
    """
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y %H:%M:%S")

# ---------------------------------------------------------------
# ETAPA 5: registrar as ferramentas
# ---------------------------------------------------------------
tools = [somar, subtrair, multiplicar, dividir, data_hora_atual]

agent = create_agent(
    model= "gpt-4.1", # requer OPENAI_API_KEY no ambiente
    tools=tools,
    system_prompt="Você é uma calculadora. Use as ferramentas disponíveis para fazer contas.",
)

# ---------------------------------------------------------------
# ETAPA 6: Permitir que o agente utilize as ferramentas para 
# responder perguntas matemáticas.
# ---------------------------------------------------------------
resultado = agent.invoke(
    {"messages": [{"role": "user", "content": "Calcule 125 x 37 e informe a data e hora do sistema."}]}
)
print(resultado["messages"][-1].content)

