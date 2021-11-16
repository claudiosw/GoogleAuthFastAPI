# GoogleAuthFastAPI

## Preparativos
1. Instale as dependências
```
pip install -r requirements.txt
```
2. Se desejar, altere o arquivo de configuração `configuracao.yaml`. A princípio não será preciso fazer nenhuma alteração.
3. Salve seu arquivo `client_secret.json` na pasta `secrets`. Se desejar, é possível alterar isto no arquivo de configuração.

## Para iniciar o webserver:
```
uvicorn main:app --reload --port=8080
```

## Para rodar:
1. Abra um navegador e digite: http://127.0.0.1:8080
2. Irá abrir uma janela pedindo autorização para acessar sua conta Google. Se você tiver mais de uma conta Google, escolha uma.
3. Irá aparecer na tela do navegador o resultado.
