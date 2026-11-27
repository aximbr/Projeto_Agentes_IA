# Desafio 02 - Primeiros Passos com LangChain

## Objetivo

Neste desafio você fará a transição da chamada direta para a API da LLM para o ecossistema LangChain.

O objetivo **não é criar um agente ainda**.

O objetivo é entender os componentes fundamentais que servirão de base para toda a arquitetura que construiremos posteriormente.

Ao final deste desafio você deverá ser capaz de:

- Instalar e configurar o LangChain
- Utilizar Chat Models
- Utilizar PromptTemplate
- Utilizar Runnable
- Separar prompt de execução
- Criar uma aplicação mais estruturada do que a do Desafio 01

---

# O Que Você Vai Aprender

## Novos Conceitos

### Chat Model

Representa uma LLM dentro do LangChain.

Exemplo:

```python
ChatOpenAI
```

---

### PromptTemplate

Permite criar prompts reutilizáveis.

Exemplo:

```text
Você é um especialista em logística.

Responda a seguinte pergunta:

{pergunta}
```

---

### Runnable

Componente executável capaz de receber entrada e produzir saída.

No LangChain moderno, praticamente tudo é um Runnable.

---

### Chain

Encadeamento de componentes.

Exemplo:

```text
Entrada
   ↓
PromptTemplate
   ↓
LLM
   ↓
Resposta
```

---

# O Que Vamos Construir

Uma aplicação simples:

```text
Usuário
   ↓
PromptTemplate
   ↓
ChatOpenAI
   ↓
Resposta
```

---

# O Que NÃO Vamos Fazer Ainda

Não utilizar:

- Agents
- Tools
- Memory
- YAML
- CSV
- Workspace
- Logs
- LangGraph
- Failover
- Benchmark

---

# Estrutura do Projeto

A estrutura principal permanece:

```text
ai-agent-platform/

├── .venv/
├── .env
├── .gitignore
├── requirements.txt
│
├── desafios/
│   ├── desafio_01/
│   └── desafio_02/
│       └── main.py
│
├── docs/
│
└── projeto_final/
```

---

# Atualização do requirements.txt

Adicionar:

```text
langchain
langchain-openai
```

Arquivo:

```text
openai
python-dotenv

langchain
langchain-openai
```

---

# Instalação

Executar:

```bash
pip install -r requirements.txt
```

---

# Tarefa 1 - Entender o Papel do LangChain

Pesquise:

- LangChain Core
- Chat Models
- PromptTemplate
- Runnable

Objetivo:

Compreender que o LangChain não substitui a LLM.

Ele organiza a interação com a LLM.

---

# Tarefa 2 - Criar o Primeiro ChatModel

Utilizar:

```python
ChatOpenAI
```

Inicialmente:

```python
model="gpt-4.1"
```

Ainda sem configurações externas.

---

# Tarefa 3 - Criar um PromptTemplate

Exemplo de estrutura:

```text
Você é um especialista em logística.

Responda a pergunta abaixo:

Pergunta:
{pergunta}
```

Objetivo:

Substituir prompts fixos por templates reutilizáveis.

---

# Tarefa 4 - Utilizar Variáveis no Prompt

Criar uma variável:

```text
pergunta
```

Exemplo:

```text
Qual a diferença entre transporte aéreo e marítimo?
```

---

# Tarefa 5 - Construir uma Chain

Fluxo:

```text
Pergunta
    ↓
PromptTemplate
    ↓
ChatOpenAI
    ↓
Resposta
```

Objetivo:

Entender como o LangChain encadeia componentes.

---

# Tarefa 6 - Utilizar invoke()

Executar a Chain.

Método:

```python
invoke()
```

Objetivo:

Entender a principal forma de execução do LangChain moderno.

---

# Saída Esperada

Exemplo:

```text
Provider: OpenAI

Model:
gpt-4.1

Pergunta:
Qual a diferença entre transporte aéreo e marítimo?

Resposta:

O transporte aéreo possui maior velocidade,
enquanto o transporte marítimo oferece maior
capacidade de carga e menor custo por tonelada.
```

---

# Tarefa 7 - Refatorar o Código

Separar responsabilidades.

Exemplo:

```text
main.py

carrega ambiente
   ↓
cria modelo
   ↓
cria prompt
   ↓
executa chain
   ↓
exibe resultado
```

Mesmo com apenas um arquivo, manter blocos organizados.

---

# Desafio Extra 01

Permitir alterar a pergunta sem alterar o código.

Utilizar:

```python
input()
```

Exemplo:

```text
Digite sua pergunta:
```

---

# Desafio Extra 02

Criar dois prompts.

Prompt 1:

```text
Especialista em Logística
```

Prompt 2:

```text
Especialista em Tecnologia
```

Observar como apenas o PromptTemplate altera a resposta.

---

# Desafio Extra 03

Criar uma função:

```python
criar_prompt(area)
```

que monta templates diferentes.

Essa ideia será utilizada posteriormente no carregamento de objetivos do agente.

---

# Critérios de Aprovação

Você concluiu o desafio quando:

- [ ] LangChain está instalado
- [ ] ChatOpenAI está funcionando
- [ ] Existe um PromptTemplate
- [ ] Existe uma variável dentro do prompt
- [ ] Existe uma Chain
- [ ] A execução utiliza invoke()
- [ ] A resposta é exibida corretamente
- [ ] Não há chamadas diretas ao SDK OpenAI

---

# O Que Deve Estar Claro ao Final

Você deve conseguir explicar:

## 1. O que é um Chat Model

Exemplo:

```python
ChatOpenAI
```

---

## 2. O que é um PromptTemplate

Exemplo:

```python
PromptTemplate(...)
```

---

## 3. O que é um Runnable

Componentes executáveis do LangChain.

---

## 4. O que é uma Chain

Fluxo encadeado de execução.

---

## 5. O que faz o método invoke()

Executa um Runnable no LangChain.

---

## 6. Por que usar LangChain

Porque ele permite:

- reutilização
- modularidade
- composição
- integração com Agents
- integração com Tools
- integração com Memory
- integração com LangGraph

---

# Relacionamento com a Arquitetura Final

Neste desafio estamos construindo a base para:

```text
Agent Builder
      ↓
Prompt Manager
      ↓
LLM Factory
      ↓
Execution Engine
```

Todos esses componentes futuros dependem dos conceitos aprendidos aqui.

---

# Resultado Esperado da Etapa

Ao final você terá:

```text
Usuário
   ↓
PromptTemplate
   ↓
ChatOpenAI
   ↓
invoke()
   ↓
Resposta
```

funcionando completamente.

---

# Próximo Desafio

## Desafio 03 - Chains e Pipelines

Objetivos:

- Criar cadeias de processamento
- Encadear múltiplas etapas
- Produzir saídas intermediárias
- Introduzir transformações antes da resposta final

Primeira aproximação da arquitetura que mais tarde permitirá construir agentes completos.