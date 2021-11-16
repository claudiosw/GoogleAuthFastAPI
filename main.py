from fastapi import FastAPI
from starlette.responses import RedirectResponse
from google.oauth import Autenticacao, OAuthInfo
from base.base import configuracao

app = FastAPI()


@app.get("/")
def home():
    aut = Autenticacao(configuracao()["GOOGLE"]["CLIENT_SECRETS"])
    authorization_url = aut.autentica_por_secrets_file()
    response = RedirectResponse(url=authorization_url)
    return response


@app.get("/v1/google-connector/authorized")
async def callback_oauth(code: str = "", state: str = "", error: str = ""):
    aut = Autenticacao("secrets/client_secret.json")
    credentials = aut.tratamento_callback(code, state, error)
    oauth_info = OAuthInfo(credentials)
    info_usuario = oauth_info.captura_info_usuario()
    return info_usuario
