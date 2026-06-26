import os
from keycloak import KeycloakOpenID

# Busca as configurações do arquivo .env local. 
# Se não existirem, mantém o padrão da rede interna do Docker (usado pela equipe)
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://keycloak:8080/")
REALM_NAME = os.getenv("REALM_NAME", "hoplife-realm")
CLIENT_ID = os.getenv("CLIENT_ID", "hoplife-backend")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "H0JI2SyAeItlsf80R5YUyWULWbTXRdIL")
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:8000/usuarios/callback/")

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    realm_name=REALM_NAME,
    client_id=CLIENT_ID,
    client_secret_key=CLIENT_SECRET,
    custom_headers={"Host": "localhost:8080"},
)