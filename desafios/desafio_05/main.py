# Projeto aprendendo a criar agentes de IA
# Author: Jose P. Leitao e co-pilot
# Data: 2026-11-27
# Nome: Desafio 05
# 
"""
Ao concluir este módulo você deverá ser capaz de:

- Explicar o que é um agente.
- Diferenciar Chain de Agent.
- Entender Tool Calling.
- Construir um agente simples em LangChain.
- Registrar ferramentas.
- Observar o processo de decisão do agente.
- Preparar a arquitetura para memória e persistência.
"""

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from tools import tools
from prompts import mensagens

# ---------------------------------------------------------------
# Ler as variaveis de ambiente
# ---------------------------------------------------------------
load_dotenv(".env")

# ---------------------------------------------------------------
# Criar o modelo (LLM)
# ---------------------------------------------------------------
llm = init_chat_model(api_key=os.environ.get("OPENAI_API_KEY"),
                      model= "gpt-4.1")

# ---------------------------------------------------------------
# Criar o agente
# ---------------------------------------------------------------
agente = create_agent(
    model=llm,
    tools=tools,
)

# ---------------------------------------------------------------
# invocar o agente com a mensagem vinda de prompt.py
# ---------------------------------------------------------------


result = agente.invoke({
    "messages": mensagens
})

print(result["messages"][-1].content)
