# Desafio 03 - Chains e Pipelines

## Objetivo

Neste desafio você aprenderá a construir fluxos compostos por múltiplas etapas utilizando LangChain.

O objetivo é compreender como dividir um problema em partes menores e encadear o processamento da informação.

Ao final deste desafio você deverá ser capaz de:

- Criar múltiplos PromptTemplates
- Encadear etapas de processamento
- Utilizar a saída de uma etapa como entrada da próxima
- Construir pipelines reutilizáveis
- Compreender a base conceitual para agentes futuros

## O Que Vamos Construir

Fluxo:

Usuário → Resumo → Análise → Relatório Final

Exemplo:

Entrada:

"A FedEx inaugurou um novo centro logístico em Campinas."

Etapa 1:
Resumo

Etapa 2:
Análise dos impactos

Etapa 3:
Relatório executivo

## Conceitos Novos

### Pipeline

Processo dividido em etapas sequenciais.

### Chain

Encadeamento de vários componentes do LangChain.

### Transformação de Contexto

Cada etapa modifica ou enriquece a informação antes de enviá-la à próxima.

## Estrutura

```text
ai-agent-platform/
└── desafios/
    └── desafio_03/
        └── main.py
```

## Tarefas

1. Criar um PromptTemplate de resumo.
2. Criar um PromptTemplate de análise.
3. Criar um PromptTemplate de relatório.
4. Encadear os três componentes.
5. Exibir os resultados intermediários.
6. Exibir o resultado final.

## Desafio Extra

Adicionar uma quarta etapa:

Classificação de Risco:

- Baixo
- Médio
- Alto

## Critérios de Aprovação

- Existe mais de uma etapa.
- A saída de uma etapa alimenta a próxima.
- O usuário visualiza o resultado final.
- O fluxo está organizado e reutilizável.

## O Que Deve Estar Claro ao Final

- Diferença entre chamada simples e pipeline.
- Benefícios de separar o processamento.
- Como encadear componentes no LangChain.

## Próximo Desafio

Desafio 04 - Ferramentas (Tools).
