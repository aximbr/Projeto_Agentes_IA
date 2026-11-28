# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-27
# Nome: Desafio 05 / prompts.py

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage

sys_mensagem = SystemMessage(
    content="Você é um assistente técnico. \
    Use ferramentas quando necessário. \
    Responda diretamente quando não precisar delas.")

user_mensagem_1 = HumanMessage(
    content="Calcule 250 x 45")

user_mensagem_2 = HumanMessage(
    content="Que horas são?")

user_mensagem_3 = HumanMessage(
    content="O que é logística reversa?")

user_mensagem_4 = HumanMessage(
    content="Calcule 10 por cento de 200")

user_mensagem_5 = HumanMessage(
    content="Qual é a temperatura na cidade de Cosmópolis?")

mensagens = [sys_mensagem, user_mensagem_5]