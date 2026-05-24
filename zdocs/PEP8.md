# Resumo do PEP 8: Guia de Estilo para Python

O **PEP 8** é o guia de estilo oficial para a escrita de código em Python. Seu objetivo principal é melhorar a legibilidade do código e torná-lo consistente em todo o ecossistema Python.

Abaixo estão as principais regras e recomendações para você incluir na sua documentação:
## 1. Ruff (Extensão do VScode)
O **Ruff** é uma extensão que pode ser instalada diretamente dentro da aba **Extensions** do Visual Studio Code. O que o ruff faz é ajudar a formatar o nosso código para o padrão PEP8 ao salvar o arquivo. 

* **Baixando o Ruff:** Para baixar o ruff basta ir na aba extensions do VScode e pesquisar Ruff.
* **Configurando o Ruff:** Para configurar o ruff basta apertar Ctrl+Shift+P no seu teclado. Isso irá abrir uma barra de pesquisa, e nessa barra você deve procurar por **Open User Settings (JSON)**. A partir desse ponto basta **adicionar uma vírgular depois da penúltima chave** e escrever o texto seguinte.
* **Texto que deve ser escrtio:** 
    "[python]": {
        "diffEditor.ignoreTrimWhitespace": false,
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit", 
            "source.organizeImports.ruff": "explicit"},
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.defaultColorDecorators": "never",
        "editor.formatOnType": true,
        "editor.wordBasedSuggestions": "off"
    }

## 2. Indentação e Espaçamento
* **Espaços em vez de Tabs:** Use sempre **4 espaços** por nível de indentação. Não misture tabs e espaços.
* **Tamanho máximo da linha:** Limite todas as linhas a um máximo de **79 caracteres**. Para docstrings ou blocos de comentários muito longos, o limite é de 72 caracteres.
* **Linhas em branco:**
  * Use **duas linhas em branco** antes de definições de funções e classes no nível superior (top-level).
  * Use **uma linha em branco** antes de definições de métodos dentro de uma classe.

## 3. Importações (Imports)
* As importações devem estar sempre no início do arquivo, logo após os comentários ou docstrings do módulo e antes das variáveis globais.
* Cada importação deve ser feita em uma linha separada.
  * **Certo:**
    ```python
    import os
    import sys
    ```
  * **Errado:** `import sys, os` (Porém, `from subprocess import Popen, PIPE` é permitido).
* A ordem de importação deve seguir estes grupos, com uma linha em branco separando-os:
  1. Bibliotecas padrão do Python (ex: `os`, `sys`, `math`).
  2. Bibliotecas de terceiros (ex: `requests`, `pandas`, `django`).
  3. Importações locais da própria aplicação/módulo.

## 4. Nomenclatura (Naming Conventions)
Manter um padrão ao nomear objetos é fundamental para identificar o que eles são:
* **Variáveis, funções e métodos:** `snake_case` (letras minúsculas com palavras separadas por sublinhado). 
  * Ex: `minha_variavel_local`, `calcular_total_da_compra()`.
* **Classes e Exceções:** `PascalCase` / `CapWords` (iniciais maiúsculas sem sublinhados). 
  * Ex: `MinhaClassePrincipal`, `UsuarioInvalidoError`.
* **Constantes:** `UPPER_SNAKE_CASE` (todas as letras maiúsculas separadas por sublinhado). 
  * Ex: `LIMITE_MAXIMO_DE_TENTATIVAS`, `TAXA_DE_JUROS`.
* **Módulos e Pacotes:** Nomes curtos e todos em minúsculas (preferencialmente sem sublinhados para pacotes). 
  * Ex: `meumodulo.py`.
* **Uso de sublinhados (`_`):** Variáveis ou métodos que começam com um sublinhado (ex: `_variavel_interna`) indicam que são de uso interno/privado (não devem ser importados usando `from modulo import *`).

## 5. Espaços em Branco em Expressões e Instruções
* **Evite espaços extras** imediatamente dentro de parênteses, colchetes ou chaves.
  * **Certo:** `spam(ham[1], {eggs: 2})`
  * **Errado:** `spam( ham[ 1 ], { eggs: 2 } )`
* Coloque um **único espaço** ao redor de operadores de atribuição (`=`), comparação (`==`, `<`, `>`, `!=`), e booleanos (`and`, `or`, `not`).
* **Atenção:** Não use espaços ao redor do sinal `=` quando ele for usado para indicar um valor padrão para um parâmetro (keyword arguments).
  * **Certo:** `def funcao(parametro=padrao):`
  * **Errado:** `def funcao(parametro = padrao):`

## 6. Comentários e Docstrings
* Comentários que contradizem o código são piores do que não ter comentários. Lembre-se de sempre atualizá-los quando o código mudar!
* Use frases completas. A primeira palavra deve ser maiúscula (a menos que seja um identificador em minúsculo).
* **Docstrings:** Utilize docstrings de aspas triplas (`""" ... """`) para documentar funções públicas, classes e módulos.

---