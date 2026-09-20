# Deploy

## Site estático

O conteúdo de `site/` pode ser publicado em GitHub Pages, Cloudflare Pages ou outro host estático.

## Worker

1. Instale Wrangler.
2. Faça `wrangler login`.
3. Copie `cloudflare/wrangler.toml.example` para `wrangler.toml`.
4. Crie o D1 e aplique `schema.sql`.
5. Configure segredos com `wrangler secret put`.
6. Faça deploy após testar localmente.

## Segurança

- Nunca comitar chaves.
- Usar variáveis de ambiente.
- Limitar endpoints.
- Validar payloads.
- Registrar erros sem dados sensíveis.
- Rotacionar tokens.
