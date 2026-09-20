# Arquitetura

## Componentes

- Coletores: APIs, RSS e Scrapy.
- Normalizador: converte fontes em um formato comum.
- Armazenamento: SQLite no protótipo; D1/PostgreSQL na produção.
- Análise: regras determinísticas primeiro; IA depois.
- Visualização: HTML, CSS e JavaScript com SVG/Canvas.
- Automação: GitHub Actions, Cloudflare Cron ou n8n.

## Registro mínimo

```json
{
  "id": "hash",
  "title": "Título",
  "url": "https://example.com/item",
  "source": "rss",
  "published_at": "2026-09-20T00:00:00Z",
  "language": "pt",
  "topics": ["robotics"],
  "relevance": 0.8,
  "confidence": "medium"
}
```

## Previsão responsável

O sistema mede sinais e gera hipóteses. Ele não promete prever o futuro. Uma hipótese exige várias fontes independentes, série histórica e experimento prático.
