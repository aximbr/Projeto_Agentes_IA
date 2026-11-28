# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-27
# Nome: Desafio 05 / tools.py

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

from langchain.tools import tool

# ---------------------------------------------------------------
# criar uma ferramenta que soma
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
# criar uma ferramenta que subtrai
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
# criar uma ferramenta que multiplica
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
# criar uma ferramenta que divide
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
# criar uma ferramenta que informe a data do sistema
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
# criar uma ferramenta que converte para maiúscula
# ---------------------------------------------------------------
@tool
def converte_para_maiusculo(texto: str) -> str:
    """Converte o texto de entrada em maiusculo

    Args:
        texto: texto a ser convertido
    """
    
    return texto.upper()

# ---------------------------------------------------------------
# criar uma ferramenta que contar caracteres
# ---------------------------------------------------------------
@tool
def contar_caracteres(texto: str) -> str:
    """Conta a quantidade de caracteres de um texto

    Args:
        texto: texto para contar os caracteres
    """
    
    return str(len(texto))

# ---------------------------------------------------------------
# criar uma ferramenta que calcula o percental de uma quantia
# ---------------------------------------------------------------
@tool
def calcular_percentual(p: float, q: float) -> str:
    """Calcula o percentual de uma quantia ou valor

    Args:
        p: o valor do percentual
        q: a quantia envolvida
    """
    
    return str(q*p/100)

# ---------------------------------------------------------------
# criar uma ferramenta que informa a temperatura de uma cidade
# ---------------------------------------------------------------
@tool
def temperatura_ficticia_cidade(cidade: str) -> str:
    """Informa a temperatura de uma cidade

    Args:
        cidade: Nome da cidade de onde quer saber a temperatura
    """
    import random
    t = random.randint(0, 55)
    return f"A temperatura em {cidade} é de {t} centigrados."

# ---------------------------------------------------------------
# ETAPA 5: registrar as ferramentas
# ---------------------------------------------------------------
tools = [somar, subtrair, multiplicar, dividir, data_hora_atual,
         converte_para_maiusculo, contar_caracteres,
         calcular_percentual, temperatura_ficticia_cidade]