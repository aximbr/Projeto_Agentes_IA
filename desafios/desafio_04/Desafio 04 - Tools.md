# Desafio 04 - Ferramentas (Tools)

## Objetivo

Neste desafio você aprenderá a fornecer capacidades externas para uma LLM.

Até agora o modelo apenas respondeu perguntas.

A partir deste desafio ele poderá executar ações através de ferramentas.

## O Que Vamos Construir

Um assistente capaz de:

- Somar
- Subtrair
- Multiplicar
- Dividir

Utilizando ferramentas registradas no LangChain.

## Conceitos Novos

### Tool

Função que pode ser chamada pelo modelo.

### Tool Calling

Capacidade do modelo decidir quando utilizar uma ferramenta.

### Separação de Responsabilidades

A LLM raciocina.

A ferramenta executa.

## Estrutura

```text
ai-agent-platform/
└── desafios/
    └── desafio_04/
        └── main.py
```

## Tarefas

### Tarefa 1

Criar uma ferramenta de soma.

### Tarefa 2

Criar uma ferramenta de subtração.

### Tarefa 3

Criar uma ferramenta de multiplicação.

### Tarefa 4

Criar uma ferramenta de divisão.

### Tarefa 5

Registrar as ferramentas no LangChain.

### Tarefa 6

Permitir que a LLM utilize as ferramentas para responder perguntas matemáticas.

Exemplo:

```text
Quanto é 125 x 37?
```

## Resultado Esperado

O modelo deverá utilizar a ferramenta adequada e retornar:

```text
4625
```

## Desafio Extra

Criar uma ferramenta:

```text
data_hora_atual
```

que retorna a data e hora do sistema.

## Critérios de Aprovação

- Existem pelo menos quatro ferramentas.
- As ferramentas estão separadas da lógica principal.
- O modelo consegue utilizá-las.
- Perguntas matemáticas produzem resultados corretos.

## O Que Deve Estar Claro ao Final

- O que é uma Tool.
- Como registrar uma Tool.
- Como a LLM decide utilizar uma Tool.
- Diferença entre conhecimento do modelo e execução de funções.

## Relacionamento com a Arquitetura Final

As futuras ferramentas do projeto utilizarão os mesmos conceitos:

- file_reader
- file_writer
- directory_list
- benchmark
- healthcheck
- workspace_manager

## Próximo Desafio

Desafio 05 - Construindo o Primeiro Agente.
