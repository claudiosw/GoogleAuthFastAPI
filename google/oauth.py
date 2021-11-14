from google_auth_oauthlib.flow import InstalledAppFlow


class Autenticacao:

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
        #self.SCOPES = ['http://127.0.0.1:8080/v1/google-connector/authorized']

    def autentica_por_secrets_file(self):
        flow = InstalledAppFlow.from_client_secrets_file(
                self.caminho_arquivo, self.SCOPES, redirect_uri="http://localhost:8080/v1/google-connector/authorized")
        flow.redirect_uri = "http://127.0.0.1:8080/v1/google-connector/authorized"
        authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # re-prompting the user for permission. Recommended for web server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')
        #flow.run_local_server(host='localhost', port=0)
        return authorization_url

