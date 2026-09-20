# Site do Radar Global

## Erro observado

Se o navegador mostra `EDB POSTGRES` e `Server is up and running`, você está acessando o servidor local do PostgreSQL/EDB na porta 8080 — não o site deste projeto.

O site do Radar deve ser executado a partir desta pasta `site/` usando o servidor Python.

## Execução correta no Windows

Na raiz do repositório:

```powershell
cd site
python server.py
```

Depois abra:

```text
http://127.0.0.1:8081/
```

A página inicial redireciona para:

```text
http://127.0.0.1:8081/dashboard.html
```

## Alternativa

```powershell
cd site
python -m http.server 8081
```

Depois abra `http://127.0.0.1:8081/`.

Use uma porta livre. Se a porta 8080 mostrar EDB/PostgreSQL, não use essa porta ou encerre o processo que já está ocupando-a.

## Verificar a pasta

Antes de iniciar, execute:

```powershell
Get-ChildItem
```

Você deve ver:

```text
index.html
dashboard.html
app.js
styles.css
```
