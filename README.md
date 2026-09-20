# Radar Global de Maquinários

Plataforma modular para acompanhar notícias, pesquisas, produtos, fornecedores, pagamentos internacionais e sinais de mercado — transformando evidências em hipóteses testáveis para criação de maquinários.

> Projeto em etapas: primeiro coletar e verificar; depois classificar; só então interpretar, alertar e prototipar.

## Objetivos

- Monitorar fontes globais por RSS, APIs e scraping responsável.
- Detectar tendências em IA, automação, tintas, revestimentos, robótica, fabricação digital, AR/VR e impressão 3D.
- Criar um histórico auditável de fontes e evidências.
- Produzir gráficos interativos e relatórios.
- Gerar hipóteses de produtos e máquinas com nível de confiança.
- Integrar Cloudflare, GitHub, Python, Scrapy e notificações.

## Princípios

1. API/RSS antes de scraping.
2. Fonte, data e URL em todo registro.
3. Deduplicação antes da análise.
4. Separar fato, inferência e hipótese.
5. Nunca tratar previsão como certeza.
6. Respeitar robots.txt, termos de uso, limites e LGPD.
7. Nenhuma chave, senha ou token no repositório.

## Pipeline

```text
RSS / GDELT / OpenAlex / páginas autorizadas
                 ↓
        coletores Python/Scrapy
                 ↓
     normalização + deduplicação
                 ↓
     banco histórico / arquivos brutos
                 ↓
 classificação de tema e relevância
                 ↓
       tendências e sinais fracos
                 ↓
 dashboard + relatório + alertas
                 ↓
 hipótese → experimento → protótipo
```

## Estrutura

```text
radar-global-maquinarios/
├── README.md
├── TODO.md
├── LICENSE
├── .gitignore
├── .env.example
├── docs/
│   ├── architecture.md
│   ├── research-method.md
│   ├── sources.md
│   ├── payments-and-residency.md
│   └── deployment.md
├── site/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── data/
│   ├── README.md
│   └── sample-signals.json
├── collectors/
│   ├── README.md
│   └── python/
│       ├── requirements.txt
│       └── collector.py
├── scraper/
│   ├── scrapy.cfg
│   └── radar_spider/
│       ├── __init__.py
│       ├── settings.py
│       └── spiders/catalogo.py
├── cloudflare/
│   ├── wrangler.toml.example
│   ├── schema.sql
│   └── worker/src/index.js
└── .github/workflows/quality.yml
```

## Como executar o site

```bash
cd site
python -m http.server 8080
```

Abra `http://localhost:8080`.

## Como testar o coletor

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
pip install -r collectors/python/requirements.txt
python collectors/python/collector.py
```

## Como testar o Scrapy

```bash
pip install scrapy
cd scraper
scrapy list
scrapy crawl catalogo -O ../data/catalogo.jsonl
```

Os seletores do spider são exemplos e precisam ser adaptados somente a fontes autorizadas.

## Fontes sugeridas

- GDELT: notícias e eventos globais.
- OpenAlex: pesquisa científica e temas emergentes.
- RSS/FreshRSS: fontes selecionadas e recorrentes.
- Scrapy: sites sem API/RSS, quando permitido.
- Cloudflare Worker/D1: API, histórico e alertas.

## Escopo financeiro

A pasta `docs/payments-and-residency.md` documenta hipóteses de arquitetura, não aconselhamento jurídico ou fiscal. A estrutura deve ser confirmada por profissionais nos países envolvidos antes de abrir empresa, mudar residência fiscal ou processar pagamentos.

## Licença

MIT. Consulte `LICENSE`.
