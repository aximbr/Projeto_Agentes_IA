# Desafio 06 - Memória Conversacional (Versão Completa)

## Visão Geral

Até o desafio anterior construímos um agente capaz de utilizar ferramentas e responder perguntas.

Porém ele sofre de uma limitação importante:

```text
Ele esquece tudo após cada interação.
```

Neste módulo faremos o agente lembrar informações fornecidas pelo usuário durante a conversa.

Este será o primeiro passo para a construção de assistentes realmente úteis.

---

# Objetivos de Aprendizado

Ao concluir este módulo você deverá ser capaz de:

- Entender o conceito de memória em agentes.
- Diferenciar conhecimento do modelo e memória da conversa.
- Implementar memória de curto prazo.
- Manter histórico de mensagens.
- Utilizar o histórico para responder perguntas futuras.
- Preparar a arquitetura para persistência em disco.

---

# Problema que Vamos Resolver

Sem memória:

Usuário:

```text
Meu nome é José.
```

Depois:

```text
Qual é o meu nome?
```

Resposta:

```text
Não sei.
```

---

Com memória:

Usuário:

```text
Meu nome é José.
```

Depois:

```text
Qual é o meu nome?
```

Resposta:

```text
Seu nome é José.
```

---

# Conceitos Fundamentais

## Memória de Curto Prazo

Mantém o histórico da conversa durante a sessão atual.

Quando a aplicação é encerrada:

```text
Memória perdida.
```

---

## Memória Persistente

Será implementada no próximo módulo.

Permanece salva mesmo após reiniciar a aplicação.

---

## Context Window

A memória não é mágica.

O histórico da conversa precisa ser enviado novamente para a LLM.

Isso aumenta:

- tokens de entrada
- custo
- latência

---

# Arquitetura da Solução

```text
Usuário
   │
   ▼
Histórico
   │
   ▼
LLM
   │
   ▼
Resposta
   │
   ▼
Atualizar Histórico
```

---

# Estrutura do Projeto

```text
ai-agent-platform/
│
└── desafios/
    └── desafio_06/
        ├── main.py
        ├── agent.py
        ├── memory.py
        └── README.md
```

---

# Tarefa 1 - Compreender o Fluxo da Conversa

Faça um desenho do ciclo:

```text
Pergunta
↓
Histórico
↓
LLM
↓
Resposta
↓
Histórico
```

Explique cada etapa.

---

# Tarefa 2 - Implementar Histórico de Mensagens

Armazene:

- mensagens do usuário
- respostas do agente

Objetivo:

Construir um histórico crescente.

---

# Tarefa 3 - Enviar Histórico para a LLM

Ao responder uma nova pergunta, envie também o histórico acumulado.

Verifique se o agente consegue lembrar informações anteriores.

---

# Tarefa 4 - Criar Sessão Interativa

Permita múltiplas perguntas.

Exemplo:

```text
> Meu nome é José
> Trabalho com logística
> Qual é o meu nome?
> Em qual área eu trabalho?
```

---

# Tarefa 5 - Limitar o Histórico

Defina um limite.

Exemplo:

```text
Últimas 10 mensagens
```

Objetivo:

Evitar crescimento infinito do contexto.

---

# Cenários de Teste

## Teste 1

```text
Meu nome é José.
```

Pergunta seguinte:

```text
Qual é o meu nome?
```

Resultado esperado:

```text
José
```

---

## Teste 2

```text
Meu gerente é Marco.
```

Pergunta:

```text
Quem é meu gerente?
```

Resultado esperado:

```text
Marco
```

---

## Teste 3

```text
Trabalho em Presidente Prudente.
```

Pergunta posterior:

```text
Onde eu trabalho?
```

Resultado esperado:

```text
Presidente Prudente
```

---

# Exercícios Extras

## Exercício 1

Criar comando:

```text
/mostrar_memoria
```

Que exibe o histórico atual.

---

## Exercício 2

Criar comando:

```text
/limpar_memoria
```

Que reinicia a conversa.

---

## Exercício 3

Exibir quantidade de mensagens armazenadas.

---

# Armadilhas Comuns

## Histórico não enviado

O agente nunca lembra nada.

Verifique se o histórico está sendo incluído na chamada à LLM.

---

## Histórico excessivo

O custo cresce rapidamente.

Mantenha limites.

---

## Informações contraditórias

Usuário:

```text
Meu nome é João.
```

Depois:

```text
Meu nome é José.
```

Observe qual informação o agente utiliza.

---

# Perguntas para Revisão

1. O que é memória conversacional?
2. O que diferencia memória de conhecimento do modelo?
3. Por que memória aumenta consumo de tokens?
4. O que é contexto?
5. Por que limitar o histórico?

---

# Critérios de Aprovação

- Histórico implementado.
- Conversa com múltiplas mensagens.
- Agente lembra informações anteriores.
- Histórico limitado.
- Compreensão dos conceitos.

---

# Relação com a Arquitetura Final

Este módulo dará origem aos componentes:

```text
memory_manager.py
conversation_history.py
session_manager.py
```

No projeto final:

```text
workspace/memory/
```

será alimentado por esses conceitos.

---

# Checklist Final

- [ ] Entendi memória conversacional.
- [ ] Consigo implementar histórico.
- [ ] Sei enviar contexto para a LLM.
- [ ] Sei limitar contexto.
- [ ] Estou preparado para persistir memória em disco.

---

# Próximo Módulo

## Desafio 07 - Persistência de Conversas

Objetivos:

- Salvar memória em arquivos.
- Recuperar memória após reiniciar a aplicação.
- Introduzir sessões.
- Preparar o caminho para memória vetorial.
