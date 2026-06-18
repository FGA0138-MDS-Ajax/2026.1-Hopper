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

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 100% |
| Itens Planejados | 0 |
| Itens Concluídos | 0 |
| Débito Técnico (%) | 0 |
| Velocidade da Equipe | 0 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 0 |
| Densidade de Defeitos | 0 |
| Casos de Teste Executados | 0 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0 |
| Desvio de Prazo (%) | 0 |

### Sprint 2

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 100% |
| Itens Planejados | 5 |
| Itens Concluídos | 4 |
| Débito Técnico (%) | 20% |
| Velocidade da Equipe | 4 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 2 |
| Densidade de Defeitos | 0 |
| Casos de Teste Executados | 1 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0% |
| Desvio de Prazo (%) | 25% |

---

### Sprint 3

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 100% |
| Itens Planejados | 5 |
| Itens Concluídos | 4 |
| Débito Técnico (%) | 20% |
| Velocidade da Equipe | 4 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 0 |
| Densidade de Defeitos | 0 |
| Casos de Teste Executados | 1 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0% |
| Desvio de Prazo (%) | 25% |

---

### Sprint 4

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 100% |
| Itens Planejados | 5 |
| Itens Concluídos | 3 |
| Débito Técnico (%) | 40% |
| Velocidade da Equipe | 3 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 1 |
| Densidade de Defeitos | 0 |
| Casos de Teste Executados | 2 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0% |
| Desvio de Prazo (%) | 37.5% |

---

### Sprint 5

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 74.4% |
| Itens Planejados | 5 |
| Itens Concluídos | 4 |
| Débito Técnico (%) | 20% |
| Velocidade da Equipe | 5 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 2 |
| Casos de Teste Executados | 2 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0% |
| Desvio de Prazo (%) | |

---

### Sprint 6

| Métrica | Valor |
| :--- | :--- |
| Taxa de conclusão da Sprint (%) | 80% |
| Itens Planejados | 6 |
| Itens Concluídos | 3 |
| Débito Técnico (%) | 0 |
| Velocidade da Equipe | 3 |
| Defeitos Encontrados | 0 |
| User Stories Implementadas | 2 |
| Densidade de Defeitos | 0 |
| Casos de Teste Executados | 0 |
| Casos de Teste Reprovados | 0 |
| Taxa de Rejeição (%) | 0% |
| Desvio de Prazo (%) | |

---

### Sprint 7

*(Replicar estrutura)*

---

### Sprint 8

*(Replicar estrutura)*

---

### Sprint 9

*(Replicar estrutura)*

---

## Histórico Consolidado

| Sprint | DT (%) | Velocidade | DD | Rejeição (%) | Desvio Prazo (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sprint 1 | 0 | 0 | 0 | 0 | 0 |
| Sprint 2 | 25% | 4 | 0 | 0% | 25% |
| Sprint 3 | 25% | 4 | 0 | 0% | 25% |
| Sprint 4 | 40% | 3 | 0 | 0% | 37.5% |
| Sprint 5 | 20% | 4 | 0 | 0% | |
| Sprint 6 | | | | | |
| Sprint 7 | | | | | |
| Sprint 8 | | | | | |
| Sprint 9 | | | | | |

---

## Registro de Testes Não Funcionais

### CT-02 — Validação de Contraste e Tamanho

#### Objetivo
Verificar se os elementos visuais do sistema possuem contraste adequado e tamanho de fonte legível para os usuários.

#### Branch
Developer 

#### Arquivos/Telas analisadas
* `base.html`
* `home.html`

#### Verificações realizadas
* Contraste entre texto e fundo da navbar;
* Contraste dos botões principais;
* Legibilidade dos textos principais;
* Tamanho das fontes;
* Responsividade da interface;
* Navegação em telas disponíveis.

#### Resultado Obtido
A interface apresentou boa legibilidade geral. Os elementos textuais possuem contraste adequado com o fundo, especialmente na navbar e nos botões principais. O uso de classes do Bootstrap contribuiu para boa responsividade e organização visual.
As fontes utilizadas apresentaram tamanho adequado para leitura confortável em desktop e dispositivos móveis.
Algumas rotas ainda utilizam placeholders (“#”), impossibilitando a validação completa de determinadas páginas em desenvolvimento.

#### Status
Aprovado parcialmente.

---

### Relatório CT-02 — Branch feature/viewth

#### Telas analisadas
* `login.html`
* `callback.html`
* `logout.html`

#### Objetivo
Validar contraste visual, tamanho dos elementos textuais e organização da interface.

#### Verificações realizadas

* **Contraste:** Os elementos textuais apresentaram contraste adequado com o fundo da interface. Os botões principais utilizaram cores destacadas e legíveis, facilitando a identificação das ações pelo usuário.
* **Tamanho das fontes:** Os títulos, textos e botões apresentaram tamanho adequado para leitura confortável. O uso de classes do Bootstrap como “display-5”, “fs-5” e “btn-lg” contribuiu positivamente para acessibilidade e usabilidade.
* **Organização visual:** A interface apresentou boa hierarquia visual, centralização adequada dos elementos e espaçamento consistente entre componentes.
* **Responsividade:** As páginas utilizam componentes responsivos do Bootstrap, apresentando boa adaptação visual para diferentes tamanhos de tela.

#### Problemas encontrados / Observações
* Alguns textos utilizam a classe “text-muted”, que pode reduzir levemente a legibilidade em determinados dispositivos ou para usuários com baixa visão.
* Recomenda-se futura adição de atributos de acessibilidade, como “aria-label”, para melhorar compatibilidade com leitores de tela.

#### Status
CT-02 aprovado para as telas analisadas na branch feature/viewth.

---

### Relatório CT-02 — Branch feature/login

#### Telas analisadas
* `base.html`
* `home.html`
* `login.html`

#### Objetivo
Validar contraste visual, tamanho de fontes, responsividade e acessibilidade das telas de login e navegação do sistema HopLife.

#### Verificações realizadas

* **Contraste:** As telas apresentaram bom contraste entre elements textuais e fundos da interface. Os botões principais utilizaram cores fortes e legíveis, facilitando a identificação das ações disponíveis ao usuário. A navbar apresentou boa legibilidade, utilizando fundo laranja com textos claros e destacados.
* **Tamanho das fontes:** Os títulos, textos e botões apresentaram tamanhos adequados para leitura confortável. O sistema utilizou classes responsivas do Bootstrap e definições de altura mínima adequadas para interação em dispositivos móveis. Os campos de entrada apresentaram boa área de clique e preenchimento visual confortável.
* **Responsividade:** A interface demonstrou boa adaptação para diferentes tamanhos de tela, utilizando grid responsivo do Bootstrap e containers adaptáveis.
* **Acessibilidade:** Foram identificadas boas práticas de acessibilidade: uso de labels explícitas; utilização de “aria-required” nos campos obrigatórios; botões com tamanho adequado; organização visual clara e consistente.

#### Problemas encontrados / Observações
* O uso de “overflow: hidden” pode limitar a navegação em telas pequenas ou em casos de zoom elevado.
* Alguns textos utilizam a classe “text-muted”, podendo reduzir levemente a legibilidade em determinados dispositivos.
* Algumas rotas ainda utilizam placeholders (“#”), impossibilitando a validação completa de determinadas funcionalidades.

#### Status
CT-02 aprovado para as telas analisadas na branch feature/login.

---

### Relatório CT-02 — Branch feature/estilizando-base-html

#### Telas analisadas
* `base.html`
* `home.html`

#### Objetivo
Validar contraste visual, tamanho dos elementos textuais, responsividade e consistência visual da interface.

#### Verificações realizadas

* **Contraste:** A navbar e o rodapé utilizam fundo escuro com texto claro, apresentando bom contraste e boa legibilidade. O link “Sair” utiliza destaque em amarelo, facilitando sua identificação.
* **Tamanho das fontes:** A branch apresenta boa preocupação com legibilidade. A navbar utiliza textos com tamanho ampliado, como “fs-5”, e a marca “HopLife” aparece com destaque visual. O rodapé também utiliza texto em tamanho confortável.
* **Responsividade:** A estrutura utiliza Bootstrap e contém botão de navegação responsiva com atributos de acessibilidade, como “aria-label”, “aria-controls” e “aria-expanded”. Isso contribui positivamente para navegação em telas menores.

#### Problemas encontrados / Observações
* O arquivo `home.html` utiliza as classes “text-warm” e “btn-warm”, mas essas classes não foram definidas no `base.html` analisado. Isso pode causar perda de estilo nos títulos e botões da página inicial.
* Existem links com placeholder “#”, como “Minhas Metas”, “Conquistas” e “Sobre o HopLife”, indicando rotas ainda não implementadas ou não conectadas.
* A branch apresenta boa legibilidade geral, mas precisa corrigir a consistência entre os estilos usados no `home.html` e os estilos definidos no `base.html`.

#### Status
CT-02 aprovado parcialmente para a branch feature/estilizando-base-html, com necessidade de ajuste nas classes de estilo utilizadas pela página inicial.

---

## Entrevistas de Validação com Usuários para o Ponto de Controle

Foram realizadas sessões de entrevista com dois usuários para avaliar a usabilidade, o layout e a clareza geral da interface do sistema. Durante os testes, buscou-se responder às seguintes questões centrais:

1. O que achou do visual e da interface do site?
2. Achou o site difícil de entender?
3. O botão de ajuda é útil?
4. Conseguiu entender bem como as metas funcionam?

Abaixo estão registrados os feedbacks e observações consolidados de cada sessão.

### Usuário 1
* **Duração da Sessão:** 18:47 minutos

**Feedback Coletado:**

* **Visual e Interface:** A interface foi avaliada de forma positiva, sendo considerada agradável e com um bom apelo visual.
* **Compreensão do Sistema:** O sistema foi considerado fácil de entender. A navegação ocorreu de forma fluida.
* **Botão de Ajuda:** O botão foi classificado como muito útil para orientar a navegação.
* **Metas e Categorias:** O usuário conseguiu compreender perfeitamente a lógica de funcionamento das metas e a estruturação das categorias propostas pelo aplicativo.

**Sugestões de Melhoria (U1):**

* Padronizar a nomenclatura: substituir menções à palavra "Hábitos" pela palavra "Metas" nas descrições do sistema, a fim de manter a consistência.
* Adicionar funcionalidades de agendamento flexível, permitindo que as metas sejam configuradas com frequência semanal, mensal ou para dias específicos da semana.
* Melhorar o texto do modal de ajuda informando que o campo de "Nome da Meta" é de formato livre (explicitar que é permitido inserir quantidades, dias ou informações textuais diversas na descrição).

### Usuário 2
* **Duração da Sessão:** 14:28 minutos

**Feedback Coletado:**

* **Visual e Interface:** O design foi elogiado por ser visualmente limpo e bem estruturado.
* **Compreensão do Sistema:** Considerou o fluxo fácil de entender e validou positivamente o objetivo geral do aplicativo. O usuário apontou que a funcionalidade de histórico é um recurso muito útil e uma excelente adição. No entanto, observou que as explicações de alguns elementos e botões clicáveis precisam ser mais claras.
* **Botão de Ajuda:** Considerou o botão de ajuda útil.
* **Metas e Categorias:** O funcionamento das metas e o propósito principal foram bem compreendidos.

**Sugestões de Melhoria (U2):**

* **Tutoriais e Ajuda:**
  * Incluir capturas de tela (imagens reais) da interface do site dentro dos slides do tutorial para melhorar o direcionamento visual do usuário.
  * Considerar mover o botão de ajuda para a parte superior da tela.
  * Ajustar a redação nos tutoriais, adicionando negrito na palavra "Hoje" (no tutorial de Minhas Metas) e incluir instruções diretas como "clicar no botão Hoje".
  * Utilizar aspas para destacar termos e seções específicas nos tutoriais (ex: referenciar abas como "Minhas Metas" na home).
  * Corrigir a concordância no modal de ajuda, alterando para "Basta clicar NO botão de interrogação".
* **Design e Navegação:**
  * Alterar a cor da borda do botão de interrogação `(?)` para a cor laranja da paleta principal, substituindo a borda verde atual para criar maior destaque.
* **Funcionalidades de Metas:**
  * Alterar a nomenclatura do campo de "Título" para "Objetivo" ou "Descrição".
  * Adicionar a possibilidade de inserir um "comentário do dia" junto ao registro diário da meta.