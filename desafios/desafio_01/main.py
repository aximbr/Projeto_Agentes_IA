# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-23
# Nome: Desafio 01
#
"""
O objetivo é entender exatamente o que acontece quando um programa Python conversa com uma LLM.
Ao final deste desafio você deverá ser capaz de:
- Ler uma chave de API a partir de um arquivo .env
- Conectar a uma LLM
- Enviar um prompt
- Receber uma resposta
- Exibir a resposta no terminal
Este desafio servirá como base para todos os demais módulos da plataforma.
"""

# Imports
import os
from dotenv import load_dotenv
from openai import OpenAI

# Ler as variaveis de ambiente
load_dotenv(".env")

# Cria o cliente da OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
# Envia as instruções para a LLM e o prompt
response = client.responses.create(
    model="gpt-4.1",
    instructions="Você é um agente prestativo",
    input="Qual a capital do Brasil?",
)

tokens_in = response.usage.input_tokens
tokens_out = response.usage.output_tokens
tokens_total = response.usage.total_tokens

print("provider: OpenAI")
print("Modelo: gpt-5.5")
print(response.output_text)

print(f"Input Tokens: {tokens_in}")
print(f"Output Tokens: {tokens_out}")
print(f"Total de Tokens: {tokens_total}")