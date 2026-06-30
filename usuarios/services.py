from keycloak import KeycloakOpenID

KEYCLOAK_URL = "http://keycloak:8080/"
REALM_NAME = "hoplife-realm"
CLIENT_ID = "hoplife-backend"
CLIENT_SECRET = "H0JI2SyAeItlsf80R5YUyWULWbTXRdIL"
REDIRECT_URI = "http://localhost:8000/usuarios/callback/"

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    realm_name=REALM_NAME,
    client_id=CLIENT_ID,
    client_secret_key=CLIENT_SECRET,
    custom_headers={"Host": "localhost:8080"},
)
