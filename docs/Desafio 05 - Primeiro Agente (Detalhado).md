# Desafio 05 - Construindo Seu Primeiro Agente

## Objetivo

Até o Desafio 04 construímos componentes isolados:

- LLM
- PromptTemplate
- Chains
- Tools

Agora vamos combinar esses elementos para construir nosso primeiro **Agent**.

Neste desafio você aprenderá o conceito mais importante de toda a plataforma.

Ao final desta etapa você terá um sistema capaz de:

- Receber um objetivo do usuário
- Decidir se precisa utilizar uma ferramenta
- Executar a ferramenta
- Analisar o resultado
- Produzir a resposta final

Este é o primeiro passo em direção à arquitetura completa que construiremos.

---

# Por Que Agentes São Diferentes?

Nos desafios anteriores o fluxo era fixo.

Exemplo:

```text
Pergunta
    ↓
Prompt
    ↓
LLM
    ↓
Resposta
```

ou

```text
Entrada
    ↓
Etapa 1
    ↓
Etapa 2
    ↓
Etapa 3
    ↓
Saída
```

O caminho era conhecido antecipadamente.

---

# O que é um Agent?

Um Agent é um componente capaz de:

```text
Pensar
↓
Decidir
↓
Executar
↓
Observar
↓
Pensar novamente
```

Uma Chain segue um fluxo fixo.

Um Agent escolhe o próximo passo dinamicamente.

---

# Exemplo

Pergunta:

```text
Quanto é 125 x 37?
```

Fluxo interno:

```text
Agent
 ↓
Preciso calcular
 ↓
Usar ferramenta Multiplicar
 ↓
Resultado = 4625
 ↓
Responder usuário
```

---

Outra pergunta:

```text
Explique o que é logística reversa.
```

Fluxo:

```text
Agent
 ↓
Não preciso de ferramenta
 ↓
Respondo diretamente
```

O comportamento muda conforme a necessidade.

---

# Conceitos Que Você Vai Aprender

## Agent

Responsável por coordenar o processo.

## Tool Selection

Capacidade de escolher ferramentas.

## Reasoning Loop

```text
Pensar
↓
Agir
↓
Observar
↓
Pensar
↓
Responder
```

---

# O Que Vamos Construir

Ferramentas:

```text
somar
subtrair
multiplicar
dividir
data_hora_atual
```

O agente deverá decidir quando utilizá-las.

---

# Estrutura do Projeto

```text
ai-agent-platform/
├── desafios/
│   └── desafio_05/
│       ├── main.py
│       ├── tools.py
│       └── README.md
├── .env
├── .venv
└── requirements.txt
```

---

# Tarefas

1. Revisar as ferramentas do Desafio 04.
2. Criar um ChatModel.
3. Construir o primeiro Agent.
4. Registrar ferramentas.
5. Criar o prompt do agente.
6. Executar perguntas matemáticas.
7. Executar perguntas conceituais.
8. Analisar quando as ferramentas foram utilizadas.

---

# Critérios de Aprovação

- Agent funcional.
- Seleção automática de ferramentas.
- Respostas corretas.
- Ferramentas reutilizáveis.
- Código organizado.

---

# O Que Deve Estar Claro Ao Final

- Diferença entre Agent e Chain.
- Tool Calling.
- Reasoning Loop.
- Delegação de tarefas para ferramentas.

---

# Próximo Módulo

## Desafio 06 - Memória Conversacional

Objetivos:

- Histórico de conversa.
- Contexto acumulado.
- Preparação para persistência.
