# Gerência de Configuração de Software (GCS)

Este documento estabelece as diretrizes e padrões adotados pela equipe para garantir a organização, a integridade e a qualidade dos artefatos desenvolvidos no projeto.

## 1. Itens de Configuração
Todos os artefatos produzidos estão sob controle de versão. Os principais itens de configuração são:

* **Código-Fonte:** Todo o código desenvolvido para a aplicação.
* **Documentação:** Arquivos Markdown que compõem o site do projeto no GitHub Pages.
* **Configurações:** Arquivos de ambiente, dependências (`requirements.txt`) e configurações de infraestrutura.
* **Modelos de Dados:** Scripts de banco de dados e diagramas.

## 2. Política de Branches (Fluxo de Trabalho)
Adotamos um fluxo baseado em **GitFlow simplificado**:

* `main`: Branch principal. Contém apenas o código estável e pronto para produção. **Não são permitidos commits diretos nesta branch.**
* `develop`: Branch de integração. É onde as novas funcionalidades são integradas antes de irem para a `main`.
* `feature/<nome-da-tarefa>`: Branches criadas para o desenvolvimento de cada nova funcionalidade ou tarefa. Sempre originadas a partir da `develop`.
* **Pull Requests (PRs):** Toda alteração deve ser enviada via Pull Request para a `develop`.

## 3. Política de Commits
Seguimos o padrão **Conventional Commits**. As mensagens devem seguir o formato: `tipo: descrição`.

**Tipos:**

* `feat`: Adição de nova funcionalidade.
* `fix`: Correção de bugs.
* `docs`: Alterações exclusivas na documentação (Markdown).
* `style`: Mudanças de formatação (PEP8) que não alteram a lógica do código.
* `refactor`: Refatoração de código sem alteração de comportamento.
* `test`: Criação de testes.

**Exemplos:**

* `feat: implementa autenticação do login via OIDC`
* `docs: atualiza sumário do projeto`
* `fix: corrige erro de conexão no SQLite`

## 4. Padrões de Código

* **Python:** Todo código deve seguir rigorosamente o guia de estilo **PEP8**.
* **Revisão:** Durante o Pull Request, deve-se verificar se o código respeita o padrão PEP8 definido. Caso contrário, o PR não deve ser aprovado.