# Radar Global de Maquinários

## Troubleshooting rápido

### Aparece EDB PostgreSQL em `localhost:8080`

Isso significa que a porta 8080 está sendo usada por outro servidor, provavelmente PostgreSQL/EDB. O site do Radar não usa essa página padrão.

Execute o servidor na pasta correta:

```powershell
cd site
python server.py
```

Depois acesse:

```text
http://127.0.0.1:8081/
```

Ou use uma porta alternativa:

```powershell
cd site
python -m http.server 8081
```

A URL `view-source:localhost:8080/index.html` mostra o código da página que está sendo servido pela porta 8080; ela não indica que o arquivo do GitHub está errado.
