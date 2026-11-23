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

Empresa ou serviço que disponibiliza acesso ao modelo.

Exemplos:

| Provider | Modelos |
|-----------|----------|
| OpenAI | GPT-4.1, GPT-4o |
| Anthropic | Claude Sonnet |
| Google | Gemini |
| Ollama | Llama, Mistral |

---

### API Key

Credencial usada para autenticar chamadas ao serviço.

A chave:

- Nunca deve ficar no código.
- Nunca deve ser enviada ao Git.
- Deve ser armazenada em um arquivo `.env`.

---

### Prompt

Texto enviado para a LLM.

Exemplo:

```text
Qual a capital do Brasil?
```

---

### Completion (Resposta)

Texto gerado pela LLM.

Exemplo:

```text
A capital do Brasil é Brasília.
```

---

# Resultado Esperado

Ao executar:

```bash
python main.py
```

O programa deverá exibir algo semelhante a:

```text
Provider: OpenAI
Model: gpt-4.1

Pergunta:
Qual a capital do Brasil?

Resposta:
A capital do Brasil é Brasília.
```

---

# Estrutura do Projeto

Crie a seguinte estrutura:

```text
desafio_01/

├── .env
├── .gitignore
├── requirements.txt
└── main.py
```

---

# Arquivo .env

Exemplo:

```ini
OPENAI_API_KEY=sua_chave_aqui
```

---

# Arquivo .gitignore

Exemplo:

```gitignore
.env

__pycache__/
*.pyc
```

---

# Arquivo requirements.txt

Exemplo:

```text
openai
python-dotenv
```

---

# Tarefa 1 - Instalar Dependências

Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

---

# Tarefa 2 - Carregar Variáveis de Ambiente

Pesquise e compreenda:

```python
from dotenv import load_dotenv
```

e

```python
os.getenv(...)
```

Objetivo:

- Carregar o arquivo `.env`
- Recuperar a chave da API
- Verificar se a chave foi encontrada

---

# Tarefa 3 - Conectar à LLM

Utilize o SDK oficial do provider escolhido.

Faça uma chamada simples utilizando o prompt:

```text
Qual a capital do Brasil?
```

---

# Tarefa 4 - Receber a Resposta

Exiba a resposta retornada pela LLM no terminal.

Exemplo:

```text
A capital do Brasil é Brasília.
```

---

# Tarefa 5 - Exibir Informações do Modelo

Antes da resposta, exiba:

```text
Provider: OpenAI
Model: gpt-4.1
```

Por enquanto essas informações podem estar definidas diretamente no código.

Mais adiante elas serão transferidas para arquivos de configuração.

---

# Critérios de Aprovação

Você concluiu o desafio se todos os itens abaixo forem verdadeiros:

- [ ] Existe um arquivo `.env`
- [ ] A API Key não está escrita no código
- [ ] Existe um `.gitignore`
- [ ] O programa conecta à LLM
- [ ] O programa envia um prompt
- [ ] O programa recebe uma resposta
- [ ] A resposta é exibida no terminal
- [ ] O provider é exibido
- [ ] O modelo é exibido

---

# Desafio Extra (Opcional)

Pesquise como obter estatísticas de uso da requisição.

Exemplo:

```text
Input Tokens: 12
Output Tokens: 8
Total Tokens: 20
```

Neste momento não é obrigatório entender todos os detalhes.

Mais tarde construiremos uma camada completa de observabilidade e auditoria.

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
- Benchmark
- Logs
- Failover
- Workspace

O objetivo é focar apenas na comunicação básica com a LLM.

---

# Dicas

Se ocorrer erro de autenticação:

```text
401 Unauthorized
```

Verifique:

- Se a variável existe no `.env`
- Se o nome da variável está correto
- Se a chave é válida

---

Se ocorrer erro de biblioteca:

```text
ModuleNotFoundError
```

Verifique:

```bash
pip install -r requirements.txt
```

---

# Conceitos que Devem Estar Claros ao Final

Você deve conseguir explicar:

1. O que é uma LLM.
2. O que é um provider.
3. O que é um model.
4. O que é uma API Key.
5. O que é um prompt.
6. O que é uma resposta da LLM.
7. Como armazenar credenciais com segurança usando `.env`.

---

# Entregável

Ao final do desafio você deve possuir apenas:

```text
desafio_01/

├── .env
├── .gitignore
├── requirements.txt
└── main.py
```

com uma execução funcional e reproduzível.

---

# Próximo Passo

Após concluir este desafio, seguiremos para:

**Desafio 02 - Primeiros Passos com LangChain**

Objetivos:

- Instalar LangChain
- Entender Chat Models
- Utilizar PromptTemplate
- Introduzir o conceito de Runnable
- Separar a chamada à LLM da lógica de negócio