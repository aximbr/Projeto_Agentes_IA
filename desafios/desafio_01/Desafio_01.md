# Desafio 01 - Seu Primeiro Contato com uma LLM

## Objetivo

Neste primeiro desafio você **não vai usar LangChain**.

O objetivo é entender exatamente o que acontece quando um programa Python conversa com uma LLM.

Ao final deste desafio você deverá ser capaz de:

- Ler uma chave de API a partir de um arquivo `.env`
- Conectar a uma LLM
- Enviar um prompt
- Receber uma resposta
- Exibir a resposta no terminal

Este desafio servirá como base para todos os demais módulos da plataforma.

---

# Importante: Ambiente Virtual Único do Projeto

Ao contrário de criar um ambiente virtual para cada desafio, utilizaremos **um único ambiente virtual compartilhado por todo o projeto**.

Isso permitirá:

- Reaproveitar dependências
- Evitar reinstalações desnecessárias
- Facilitar a evolução para os próximos desafios
- Utilizar a mesma base até a arquitetura final

---

# Estrutura Geral do Projeto

Crie a seguinte estrutura:

```text
ai-agent-platform/

├── .venv/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── docs/
│
├── desafios/
│   ├── desafio_01/
│   │   └── main.py
│   │
│   ├── desafio_02/
│   └── ...
│
└── projeto_final/
```

---

# Criando o Ambiente Virtual

Na raiz do projeto:

```bash
python -m venv .venv
```

---

# Ativando o Ambiente

## Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

---

## Linux / macOS

```bash
source .venv/bin/activate
```

---

# Arquivo requirements.txt

Na raiz do projeto:

```text
openai
python-dotenv
```

---

# Instalando Dependências

Com o ambiente ativado:

```bash
pip install -r requirements.txt
```

---

# Arquivo .env

Na raiz do projeto:

```ini
OPENAI_API_KEY=sua_chave_aqui
```

---

# Arquivo .gitignore

Na raiz do projeto:

```gitignore
.env

.venv/

__pycache__/
*.pyc
```

---

# Estrutura do Desafio 01

```text
ai-agent-platform/

├── .venv/
├── .env
├── .gitignore
├── requirements.txt
│
├── desafios/
│   └── desafio_01/
│       └── main.py
│
└── docs/
```

---

# O que Você Vai Aprender

## Conceitos

### LLM (Large Language Model)

Modelo de linguagem capaz de compreender e gerar texto.

Exemplos:

- GPT-4.1
- GPT-4o
- Claude Sonnet
- Gemini
- Llama

---

### Provider

Empresa que disponibiliza acesso ao modelo.

Exemplos:

| Provider | Modelos |
|-----------|----------|
| OpenAI | GPT-4.1 |
| Anthropic | Claude Sonnet |
| Google | Gemini |
| Ollama | Llama |

---

### API Key

Credencial usada para autenticar chamadas.

Ela deverá ficar:

✅ No `.env`

❌ Nunca no código

❌ Nunca no Git

---

### Prompt

Mensagem enviada à LLM.

Exemplo:

```text
Qual a capital do Brasil?
```

---

### Completion

Resposta gerada pela LLM.

Exemplo:

```text
A capital do Brasil é Brasília.
```

---

# Tarefa 1 - Validar o Ambiente

Verifique:

```bash
python --version
```

e

```bash
pip list
```

Confirme que:

- o ambiente virtual está ativo;
- as bibliotecas foram instaladas.

---

# Tarefa 2 - Carregar Variáveis do .env

Pesquise sobre:

```python
load_dotenv()
```

e

```python
os.getenv()
```

Objetivo:

- carregar o `.env`;
- recuperar a API Key.

---

# Tarefa 3 - Conectar à OpenAI

Utilize o SDK oficial.

Prompt:

```text
Qual a capital do Brasil?
```

---

# Tarefa 4 - Receber a Resposta

Exiba o conteúdo retornado.

Exemplo:

```text
A capital do Brasil é Brasília.
```

---

# Tarefa 5 - Exibir Informações do Modelo

Antes da resposta:

```text
Provider: OpenAI
Model: gpt-4.1
```

Por enquanto essas informações podem estar fixas no código.

Mais tarde elas serão carregadas por configuração.

---

# Saída Esperada

```text
Provider: OpenAI
Model: gpt-4.1

Pergunta:
Qual a capital do Brasil?

Resposta:
A capital do Brasil é Brasília.
```

---

# Critérios de Aprovação

Você concluiu o desafio quando:

- [ ] Existe um ambiente virtual único na raiz do projeto
- [ ] O ambiente virtual está funcionando
- [ ] Existe um arquivo `.env`
- [ ] A API Key não está no código
- [ ] Existe um `.gitignore`
- [ ] O programa conecta à LLM
- [ ] O programa envia um prompt
- [ ] O programa recebe uma resposta
- [ ] A resposta é exibida no terminal
- [ ] Provider é exibido
- [ ] Modelo é exibido

---

# Desafio Extra (Opcional)

Pesquise como obter:

- Input Tokens
- Output Tokens
- Total Tokens

Exemplo:

```text
Input Tokens: 15
Output Tokens: 12
Total Tokens: 27
```

Não é obrigatório implementar.

Iremos construir uma camada completa de métricas e observabilidade nos desafios futuros.

---

# O Que NÃO Fazer Neste Desafio

Não utilizar:

- LangChain
- LangGraph
- Agents
- Tools
- Memory
- YAML
- CSV
- Workspace
- Failover
- Fallback
- Benchmark
- Logs

O foco é apenas compreender a comunicação direta com uma LLM.

---

# Conceitos que Devem Estar Claros ao Final

Você deve conseguir explicar:

1. O que é uma LLM.
2. O que é um Provider.
3. O que é um Model.
4. O que é uma API Key.
5. O que é um Prompt.
6. O que é uma Completion.
7. Como utilizar um ambiente virtual Python.
8. Como armazenar credenciais usando `.env`.
9. Como instalar dependências usando `requirements.txt`.

---

# Entregável

Ao final do desafio você deverá possuir:

```text
ai-agent-platform/

├── .venv/
├── .env
├── .gitignore
├── requirements.txt
│
├── desafios/
│   └── desafio_01/
│       └── main.py
│
└── docs/
```

com uma execução funcional e reproduzível.

---

# Próximo Passo

Após concluir este desafio avançaremos para:

## Desafio 02 - Primeiros Passos com LangChain

Objetivos:

- Instalar LangChain
- Compreender Chat Models
- Entender PromptTemplate
- Criar o primeiro Runnable
- Separar a chamada da LLM da lógica da aplicação