# HopLife – Registro de Coleta de Métricas (GQM)

## Objetivo

Este documento tem como finalidade registrar os valores coletados das métricas definidas no Plano GQM do projeto HopLife.

A coleta deve ser realizada ao final de cada Sprint durante a Sprint Review ou Retrospective.

Os dados registrados servirão como evidência para análise da evolução do projeto e para apoiar decisões de replanejamento quando necessário.

---

## Resumo Rápido de Coleta

### Métrica 1 – Débito Técnico (DT)

#### O que medir?

Quantidade de itens planejados que não foram concluídos na Sprint.

#### Como coletar?

1. Contar quantos itens foram planejados na Sprint.
2. Contar quantos itens foram concluídos.
3. Aplicar a fórmula:

DT = ((Planejados - Concluídos) / Planejados) × 100

#### Valor esperado

≤ 20%

#### Exemplo

Planejados: 10

Concluídos: 8

DT = ((10 - 8) / 10) × 100

DT = 20%

---

### Métrica 2 – Velocidade da Equipe

#### O que medir?

Quantidade de itens concluídos na Sprint.

#### Como coletar?

Contar quantas User Stories ou itens do backlog foram concluídos.

#### Valor esperado

Estável ou crescente entre as Sprints.

#### Exemplo

Sprint 1 → 4 itens

Sprint 2 → 5 itens

Sprint 3 → 6 itens

---

### Métrica 3 – Densidade de Defeitos (DD)

#### O que medir?

Quantidade de defeitos encontrados para cada User Story implementada.

#### Como coletar?

1. Contar os defeitos encontrados nos testes.
2. Contar as User Stories implementadas.
3. Aplicar a fórmula:

DD = Defeitos Encontrados / User Stories Implementadas

#### Valor esperado

≤ 1 defeito por US

#### Exemplo

4 defeitos encontrados

5 User Stories implementadas

DD = 4 / 5

DD = 0,8

---

### Métrica 4 – Taxa de Rejeição de Testes

#### O que medir?

Percentual de casos de teste reprovados.

#### Como coletar?

1. Contar os casos de teste executados.
2. Contar os casos reprovados.
3. Aplicar a fórmula:

TR = (Casos Reprovados / Casos Executados) × 100

#### Valor esperado

≤ 10%

#### Exemplo

20 testes executados

2 testes reprovados

TR = (2 / 20) × 100

TR = 10%

---

### Métrica 5 – Desvio de Prazo

#### O que medir?

Percentual de atraso da Sprint.

#### Como coletar?

1. Registrar a data planejada.
2. Registrar a data real.
3. Calcular a diferença em dias.
4. Aplicar a fórmula:

DP = ((Data Real - Data Planejada) / Duração da Sprint) × 100

#### Valor esperado

0%

#### Tolerância

Até 10%

#### Exemplo

Sprint prevista para 8 dias

Entrega ocorreu 1 dia depois

DP = (1 / 8) × 100

DP = 12,5%

---

## Registro das Coletas

### Sprint 1


| Métrica                    | Valor |
| -------------------------- | ----- |
| Itens Planejados           |0       |
| Itens Concluídos           | 0      |
| Débito Técnico (%)         |  0     |
| Velocidade da Equipe       |   0    |
| Defeitos Encontrados       |    0   |
| User Stories Implementadas |     0  |
| Densidade de Defeitos      |0       |
| Casos de Teste Executados  | 0      |
| Casos de Teste Reprovados  |  0     |
| Taxa de Rejeição (%)       |   0    |
| Desvio de Prazo (%)        |    0   |

#### Análise

* Meta de DT atendida? ( ) Sim ( ) Não
* Meta de DD atendida? ( ) Sim ( ) Não
* Meta de Rejeição atendida? ( ) Sim ( ) Não
* Meta de Prazo atendida? ( ) Sim ( ) Não

#### Observações: 

* Sprint dedicada ao setup do ambiente de desenvolvimento, então não houve coleta de dados.

### Sprint 2

| Métrica                    | Valor |
| -------------------------- | ----- |
| Itens Planejados           |5       |
| Itens Concluídos           | 4      |
| Débito Técnico (%)         |  25%     |
| Velocidade da Equipe       |   4    |
| Defeitos Encontrados       |    0   |
| User Stories Implementadas |     2  |
| Densidade de Defeitos      |0       |
| Casos de Teste Executados  | 1      |
| Casos de Teste Reprovados  |  0     |
| Taxa de Rejeição (%)       |   0%    |
| Desvio de Prazo (%)        |    25%   |

#### Análise

* Meta de DT atendida? ( ) Sim (X) Não
* Meta de DD atendida? (X) Sim ( ) Não
* Meta de Rejeição atendida? (X) Sim ( ) Não
* Meta de Prazo atendida? ( ) Sim (X) Não

#### Observações:

* Durante a sprint ocorreram atrasos no desenvolvimento das interfaces

---

### Sprint 3

| Métrica                    | Valor |
| -------------------------- | ----- |
| Itens Planejados           |5       |
| Itens Concluídos           | 3      |
| Débito Técnico (%)         |  40%     |
| Velocidade da Equipe       |   3    |
| Defeitos Encontrados       |    0   |
| User Stories Implementadas |     1  |
| Densidade de Defeitos      |0       |
| Casos de Teste Executados  | 0      |
| Casos de Teste Reprovados  |  0     |
| Taxa de Rejeição (%)       |   0%    |
| Desvio de Prazo (%)        |    25%   |

#### Análise

* Meta de DT atendida? ( ) Sim (X) Não
* Meta de DD atendida? (X) Sim ( ) Não
* Meta de Rejeição atendida? () Sim () Não
* Meta de Prazo atendida? ( ) Sim (X) Não

#### Observações: 

* Durante a sprint novamente ocorreram atrasos no deselvolvimento das interfaces e do front-end.
* O teste agendado para a sprint 2 ainda não foi realizado.

---

### Sprint 4

Em andamento (Será atualizado após o Sprint Review)

---

### Sprint 5

(Replicar estrutura)

---

### Sprint 6

(Replicar estrutura)

---

### Sprint 7

(Replicar estrutura)

---

### Sprint 8

(Replicar estrutura)

---

### Sprint 9

(Replicar estrutura)

---

## Histórico Consolidado

| Sprint   | DT (%) | Velocidade | DD | Rejeição (%) | Desvio Prazo (%) |
| -------- | ------ | ---------- | -- | ------------ | ---------------- |
| Sprint 1 |   0     |    0        |  0  |      0        |      0            |
| Sprint 2 |  25%      |      4      |  0  |    0%          |       25%           |
| Sprint 3 |    40%    |    3        |  0  |      0%        |        25%          |
| Sprint 4 |        |            |    |              |                  |
| Sprint 5 |        |            |    |              |                  |
| Sprint 6 |        |            |    |              |                  |
| Sprint 7 |        |            |    |              |                  |
| Sprint 8 |        |            |    |              |                  |
| Sprint 9 |        |            |    |              |                  |

---
