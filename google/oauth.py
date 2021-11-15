from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Autenticacao:

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email',
                       'https://www.googleapis.com/auth/userinfo.profile']
        self.redirect_url = "http://127.0.0.1:8080/v1/google-connector/authorized"

    def autentica_por_secrets_file(self):
        flow = InstalledAppFlow.from_client_secrets_file(
                self.caminho_arquivo, self.SCOPES)
        flow.redirect_uri = self.redirect_url
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')
        return authorization_url

    def tratamento_callback(self, code, state, error):
        if error == "access_denied":
            return "Accesso Negado"
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.caminho_arquivo,
                scopes=self.SCOPES,
                redirect_uri=self.redirect_url
            )
            flow.fetch_token(code=code)
            return flow.credentials


class OAuthInfo:

    def __init__(self, credentials):
        self.credentials = credentials

    def captura_info_usuario(self):
        oauth2_client = build('oauth2', 'v2', credentials=self.credentials)
        info_usuario = oauth2_client.userinfo().get().execute()
        return {"first_name": info_usuario["given_name"],
                "last_name": info_usuario["family_name"],
                "photo_url": info_usuario["picture"],
                "email": info_usuario["email"]}
