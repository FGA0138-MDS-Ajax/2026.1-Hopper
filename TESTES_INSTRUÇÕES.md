# 📋 Instruções para Executar os Testes - HopLife

## 📌 Resumo dos Testes Implementados

Foram implementados **2 novos testes** para o aplicativo `metas` do projeto HopLife, mantendo todos os 10 testes antigos. **Total: 18 testes funcionales!**

### ✅ Testes Antigos (Já Existentes)
- `MetasModelsTest`: 4 testes de modelo de dados
- `MetasViewsTest`: 8 testes de views e integrações

### 🆕 Novos Testes

#### **CT-03 – Cadastro e Visualização de Metas** (Teste de Integração) ✅
- **Classe**: `TestCT03CadastroeVisualizacaoMetas`
- **Tipo**: `django.test.TestCase`
- **Quantidade**: 2 testes
- **O que testa**:
  - Usuário autenticado cria uma nova meta
  - Sistema redireciona para a listagem
  - Meta aparece com título correto
  - Status padrão é "branco" (emoji ⬜)
  - HTML renderizado com emoji correto

#### **CT-04 – Marcação Diária de Meta Cumprida** (Teste de Funcionalidade) ✅
- **Classe**: `TestCT04MarcacaoDiariaMetaCumprida`
- **Tipo**: `django.test.TestCase` (testando requisição POST)
- **Quantidade**: 4 testes
- **O que testa**:
  - Requisição POST para atualizar status funciona
  - Banco de dados é atualizado corretamente
  - Status '⬜' → '✅' → '❌' → '⬜'
  - HTML renderiza emojis corretos após cada alteração
  - Múltiplas transições de estado funcionam

#### **CT-04 Com Selenium** (Teste E2E com Browser Real - BÔNUS)
- **Classe**: `TestCT04MarcacaoDiariaMetaCumpridaComSelenium`
- **Tipo**: `django.contrib.staticfiles.testing.StaticLiveServerTestCase`
- **O que testa** (opcional):
  - JavaScript executa (fetch API)
  - DOM atualiza em tempo real sem refresh
  - Modal abre e fecha corretamente
  - Interação completa do usuário com browser real
- **⚠️ Requer**: Google Chrome instalado e configuração adicional

---

## 🎯 Como Executar os Testes

### **COMANDO PRINCIPAL: Rodar todos os testes principais** ✅
```bash
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida
```
**Resultado esperado**: `Ran 18 tests in ~60s ... OK`

---

### **1️⃣ Rodar TODOS os testes da pasta `metas` (excluindo Selenium)**
```bash
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida
```

### **2️⃣ Rodar apenas testes antigos (compatibilidade)**
```bash
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest
```

### **3️⃣ Rodar apenas CT-03**
```bash
python manage.py test metas.tests.TestCT03CadastroeVisualizacaoMetas --verbosity=2
```

### **4️⃣ Rodar apenas CT-04 (POST e DOM)**
```bash
python manage.py test metas.tests.TestCT04MarcacaoDiariaMetaCumprida --verbosity=2
```

### **5️⃣ Rodar um método específico**
```bash
# Exemplo: Apenas teste de cadastro
python manage.py test metas.tests.TestCT03CadastroeVisualizacaoMetas.test_cadastro_meta_com_visualizacao_sucesso
```

### **6️⃣ Rodar com verbosidade (mais detalhes)**
```bash
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida -v 2
```

### **7️⃣ Rodar teste com Selenium (OPCIONAL - requer Chrome)**
```bash
python manage.py test metas.tests.TestCT04MarcacaoDiariaMetaCumpridaComSelenium -v 2
```

### **8️⃣ Parar na primeira falha (para debug)**
```bash
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida --failfast
```

---

## ⚙️ Dependências Necessárias

### Já Instaladas ✅
- **Django**: 6.0.5
- **Selenium**: 4.15.2 (adicionado ao `requirements.txt`)

### Pré-requisitos do Sistema
- **Python**: 3.8+
- **Google Chrome**: Necessário apenas se rodar teste Selenium

---

## 🔍 Entendendo os Resultados

### ✅ Sucesso Esperado
```
Ran 18 tests in 60.898s

OK
Destroying test database for alias 'default'...
```

### ⚠️ Se Falhar
```
FAILED (failures=1, errors=0)
```

### 📊 Saída Detalhada (com -v 2)
```
test_cadastro_meta_com_visualizacao_sucesso (metas.tests.TestCT03CadastroeVisualizacaoMetas)
Critério de Aceitação: A meta deve ser cadastrada e exibida com sucesso. ... ok

test_marcacao_meta_sucesso_atualiza_banco (metas.tests.TestCT04MarcacaoDiariaMetaCumprida)
Teste 1: Validar que POST para atualizar meta funciona ... ok
```

---

## 📝 Estrutura do Arquivo `tests.py`

```
metas/tests.py
├── MetasModelsTest (4 testes)
│   ├── test_categoria_str
│   ├── test_meta_str
│   ├── test_dias_do_mes_atual_cria_registros
│   └── test_registro_diario_property_hoje
│
├── MetasViewsTest (8 testes)
│   ├── test_listar_metas_view
│   ├── test_criar_meta_view
│   ├── test_deletar_meta_view
│   ├── test_atualizar_status_diario_sucesso
│   ├── test_atualizar_status_diario_invalido
│   ├── test_criar_categoria_view
│   ├── test_listar_categorias_view
│   └── test_deletar_categoria_view
│
├── TestCT03CadastroeVisualizacaoMetas (2 testes) ⭐ NOVO
│   ├── test_cadastro_meta_com_visualizacao_sucesso
│   └── test_cadastro_meta_sem_categoria
│
└── TestCT04MarcacaoDiariaMetaCumprida (4 testes) ⭐ NOVO
    ├── test_marcacao_meta_sucesso_atualiza_banco
    ├── test_marcacao_meta_falha
    ├── test_marcacao_meta_limpar
    └── test_listagem_exibe_emoji_correto
```

---

## 🚀 Dica para o Líder do Grupo

Para rodar e validar antes de entregar:

```bash
# Teste rápido (18 testes, ~60 segundos)
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida

# Teste com relatório detalhado
python manage.py test metas.tests.MetasModelsTest metas.tests.MetasViewsTest metas.tests.TestCT03CadastroeVisualizacaoMetas metas.tests.TestCT04MarcacaoDiariaMetaCumprida -v 2 --failfast
```

---

## 📚 Referências

- [Documentação Django Testing](https://docs.djangoproject.com/en/6.0/topics/testing/)
- [Django TestCase API](https://docs.djangoproject.com/en/6.0/ref/test-utils/client/)
- [Selenium Python Documentation](https://www.selenium.dev/documentation/webdriver/)

---

## ✨ O que foi implementado

### ✅ CT-03: Integração Completa
- Testa criação de meta via formulário
- Valida redirecionamento após sucesso
- Confirma renderização no HTML
- Valida status padrão ⬜

### ✅ CT-04: Funcionalidade POST + DOM
- Testa requisição POST assíncrona
- Valida atualização do banco de dados
- Confirma renderização correta dos emojis
- Testa múltiplas transições de estado

### 🎁 Bônus: Teste Selenium
- Simula browser real
- JavaScript execution (fetch API)
- Interação completa do usuário
- Validação E2E

---

**Última atualização**: 2026-06-23  
**Versão**: 2.0 (Validada)  
**Status**: ✅ **PRONTO PARA PRODUÇÃO**  
**Total de Testes**: 18 ✅  
**Testes Novos**: 6 (CT-03: 2, CT-04: 4)  
**Tempo Execução**: ~60 segundos (sem Selenium)

