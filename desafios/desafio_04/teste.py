# pip install -U langchain langchain-openai
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool

# "Banco de dados" simples só para o exemplo
CATALOGO = {
    "caderno": 15.90,
    "caneta": 3.50,
    "mochila": 89.90,
}


# ---------------------------------------------------------
# PASSO 1: definir a ferramenta com @tool
# - Type hints (str aqui) são OBRIGATÓRIOS: viram o esquema
#   de argumentos que o modelo preencherá
# - A docstring ensina o modelo QUANDO e COMO usar a tool
# ---------------------------------------------------------
@tool
def consultar_preco(produto: str) -> str:
    """Consulta o preço de um produto no catálogo da loja.

    Args:
        produto: nome do produto (ex.: "caderno", "mochila")
    """
    preco = CATALOGO.get(produto.lower())
    if preco is None:
        return f"Produto '{produto}' não encontrado no catálogo."
    return f"O preço de {produto} é R$ {preco:.2f}."


# ---------------------------------------------------------
# PASSO 2: criar o agente passando a ferramenta
# ---------------------------------------------------------
modelo = init_chat_model("gpt-5.4")

agente = create_agent(
    modelo,
    tools=[consultar_preco],
    system_prompt="Você é um assistente de vendas. Consulte o preço com a ferramenta antes de responder.",
)

# ---------------------------------------------------------
# PASSO 3: conversar com o agente
# O modelo lê a pergunta, decide chamar consultar_preco,
# recebe o resultado e responde ao usuário
# ---------------------------------------------------------
resultado = agente.invoke({
    "messages": [{"role": "user", "content": "Quanto custa uma mochila?"}]
})
print(resultado["messages"][-1].content)