# Desafio 05 - Construindo Seu Primeiro Agente (Versão Completa)

## Visão Geral

Este módulo marca a transição mais importante do curso. Até agora construímos componentes isolados: modelos, prompts, chains e ferramentas. A partir deste desafio começaremos a construir sistemas capazes de tomar decisões.

O objetivo não é criar um agente complexo. O objetivo é compreender profundamente o padrão de funcionamento dos agentes modernos para que os próximos módulos (memória, persistência, logs, YAML, workspace e LangGraph) façam sentido.

---

# Objetivos de Aprendizado

Ao concluir este módulo você deverá ser capaz de:

- Explicar o que é um agente.
- Diferenciar Chain de Agent.
- Entender Tool Calling.
- Construir um agente simples em LangChain.
- Registrar ferramentas.
- Observar o processo de decisão do agente.
- Preparar a arquitetura para memória e persistência.

---

# Teoria

## Chain

Uma Chain possui fluxo previsível.

```text
Entrada
 ↓
Prompt
 ↓
LLM
 ↓
Saída
```

A sequência já é conhecida antes da execução.

## Agent

Um Agent escolhe dinamicamente o próximo passo.

```text
Pergunta
 ↓
Análise
 ↓
Preciso de ferramenta?
 ↓
Sim / Não
 ↓
Ferramenta
 ↓
Resposta
```

---

# Padrão ReAct

Grande parte dos agentes modernos segue o conceito:

```text
Reason
↓
Act
↓
Observe
↓
Reason
```

O agente avalia o problema, executa uma ação, observa o resultado e decide o próximo passo.

---

# Arquitetura da Solução

```text
Usuário
  │
  ▼
Agent
  │
  ├── Pensar
  │
  ├── Escolher Ferramenta
  │
  ├── Executar Ferramenta
  │
  └── Produzir Resposta
         │
         ▼
      Usuário
```

---

# Estrutura de Diretórios

```text
ai-agent-platform/
│
├── desafios/
│   └── desafio_05/
│       ├── main.py
│       ├── tools.py
│       ├── prompts.py
│       └── README.md
│
├── .env
├── requirements.txt
└── .venv/
```

---

# Ferramentas Obrigatórias

Implementar:

```text
somar
subtrair
multiplicar
dividir
data_hora_atual
```

Cada ferramenta deve possuir:

- nome claro
- descrição clara
- responsabilidade única

---

# Fluxos de Teste

## Cenário 1

Entrada:

```text
Quanto é 250 x 45?
```

Esperado:

- agente usa multiplicar
- retorna 11250

## Cenário 2

Entrada:

```text
Que horas são?
```

Esperado:

- agente usa data_hora_atual

## Cenário 3

Entrada:

```text
O que é logística reversa?
```

Esperado:

- resposta direta
- sem uso de ferramentas

---

# Tarefa 1 - Revisar as Ferramentas

Garanta que todas as ferramentas do Desafio 04 estejam funcionando isoladamente.

Teste cada uma manualmente.

---

# Tarefa 2 - Criar o Modelo

Utilize um ChatModel compatível com Tool Calling.

Objetivo:

- compreender como o Agent interage com a LLM
- preparar o ambiente para decisões dinâmicas

---

# Tarefa 3 - Criar o Prompt do Agente

Exemplo conceitual:

```text
Você é um assistente técnico.
Use ferramentas quando necessário.
Responda diretamente quando não precisar delas.
```

Experimente diferentes versões.

---

# Tarefa 4 - Criar o Agent

Utilize o mecanismo de Agent do LangChain.

Objetivos:

- registrar ferramentas
- associar ferramentas ao modelo
- permitir tomada de decisão

---

# Tarefa 5 - Executar Testes

Executar pelo menos:

- cálculo
- consulta de data/hora
- pergunta conceitual

Registrar observações.

---

# Exercícios Extras

## Exercício 1

Criar ferramenta:

```text
converter_para_maiusculo
```

## Exercício 2

Criar ferramenta:

```text
contar_caracteres
```

## Exercício 3

Criar ferramenta:

```text
calcular_percentual
```

## Exercício 4

Criar ferramenta:

```text
temperatura_ficticia_cidade
```

(sem API externa)

Objetivo: praticar criação de ferramentas.

---

# Perguntas para Revisão

Explique com suas palavras:

1. O que é um Agent?
2. Como ele difere de uma Chain?
3. O que é Tool Calling?
4. O que é Reasoning Loop?
5. Em quais situações uma ferramenta deve ser usada?
6. O que acontece quando uma ferramenta retorna um resultado inesperado?

---

# Armadilhas Comuns

## Ferramenta nunca utilizada

Possíveis causas:

- descrição inadequada
- prompt inadequado
- ferramenta não registrada

## Ferramenta incorreta

O agente escolhe uma ferramenta errada.

Analise:

- descrição da ferramenta
- instruções do sistema

## Resposta sem ferramenta

Alguns modelos resolvem problemas simples sem chamar ferramentas.

Ajuste o prompt para incentivar o uso correto.

---

# Critérios de Aprovação

- Agente funcional.
- Ferramentas registradas.
- Tool Calling funcionando.
- Testes executados.
- Código organizado.
- Entendimento dos conceitos.

---

# Como Este Módulo se Conecta à Arquitetura Final

A arquitetura futura será:

```text
Agent
 ↓
Memory
 ↓
Tools
 ↓
Workspace
 ↓
Logs
 ↓
Validation
 ↓
Benchmark
```

O componente central continua sendo o Agent.

---

# Checklist Final

- [ ] Entendi o conceito de Agent.
- [ ] Sei explicar Tool Calling.
- [ ] Sei registrar ferramentas.
- [ ] Sei observar as decisões do agente.
- [ ] Consigo diferenciar Agent e Chain.
- [ ] Estou pronto para adicionar memória.

---

# Próximo Módulo

## Desafio 06 - Memória Conversacional

No próximo módulo faremos o agente lembrar informações fornecidas anteriormente e introduziremos o conceito de contexto persistente.
