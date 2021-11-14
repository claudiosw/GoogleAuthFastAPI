from fastapi import FastAPI
from google.oauth import Autenticacao

app = FastAPI()


@app.get("/")
def home():
    aut = Autenticacao("secrets/client_secret.json")
    creds = aut.autentica_por_secrets_file()
    return {"Hello": creds}
