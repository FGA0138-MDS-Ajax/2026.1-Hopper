# 📚 Documentação Oficial — HopLife

Este espaço é dedicado exclusivamente à gestão, escrita e publicação da documentação do projeto **HopLife**. Utilizamos o **MkDocs** com o tema **Material** para gerar o nosso site estático de forma automatizada.

O site oficial da nossa documentação pode ser acessado em:  
🌐 (https://fga0138-mds-ajax.github.io/2026.1-Hopper/)

---

## 📁 Estrutura de Arquivos

A organização desta branch segue a estrutura necessária para o funcionamento da esteira de Integração Contínua (CI):

```text
├── .github/workflows/ci.yml # Robô de automação do deploy
├── zdocs/                   # Todos os arquivos .md e imagens da documentação
│   ├── arquiteturaimgs/     # Imagens e diagramas de arquitetura
│   ├── visaoimgs/           # Imagens do documento de visão
│   ├── index.md             # Página inicial da documentação
│   └── visao.md             # Documento de Visão
│   ├── arquitetura.md       # Documento de Arquitetura de Software
|   └── PEP8.md              # Documento que explicativo sobre o PEP8 e guia de como utilizar o Ruff
|   └── configuracoes.md     # Documento que define os itens de configuração e as políticas de branches e commits
|   └── relatorios.md     # Documento que exibe os dados coletados durante as sprints
└── mkdocs.yml               # Arquivo de configuração global do MkDocs