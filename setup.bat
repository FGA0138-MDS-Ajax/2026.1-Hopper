@echo off
chcp 65001 >nul
echo =========================================================
echo  Iniciando o setup automatico do HopLife...
echo =========================================================

:: 1. Cria o arquivo .env a partir do exemplo (se ele não existir)
IF NOT EXIST .env (
    echo [1/4] Criando arquivo .env local...
    copy .env.example .env >nul
) ELSE (
    echo [1/4] Arquivo .env ja existe. Pulando etapa...
)

:: 2. Cria o ambiente virtual
echo [2/4] Criando o ambiente virtual (venv)...
python -m venv venv

:: 3. Ativa o ambiente virtual e instala dependencias
echo [3/4] Instalando dependencias locais para o VS Code...
call venv\Scripts\activate.bat
pip install -r requirements.txt

:: 4. Sobe os conteineres do Docker
echo [4/4] Construindo e subindo os conteineres no Docker...
docker-compose up -d --build

echo =========================================================
echo  SETUP CONCLUIDO COM SUCESSO!
echo  O seu projeto HopLife ja esta rodando em: http://localhost:8000
echo  Lembre-se de selecionar a 'venv' como interpretador no VS Code!
echo =========================================================
pause