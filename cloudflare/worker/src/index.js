function json(data, status = 200) { return new Response(JSON.stringify(data), {status, headers: {'content-type': 'application/json;charset=UTF-8'}}); }

export default {
  async fetch(request, env) {
    if (request.method === 'GET') {
      const { results } = await env.DB.prepare('SELECT * FROM signals ORDER BY collected_at DESC LIMIT 100').all();
      return json(results);
    }
    if (request.method !== 'POST') return json({error:'method not allowed'},405);
    const body = await request.json();
    if (!body.title) return json({error:'title required'},400);
    await env.DB.prepare('INSERT INTO signals (title,url,source,published_at,topic,score,confidence,collected_at) VALUES (?,?,?,?,?,?,?,datetime(\'now\'))').bind(body.title,body.url||null,body.source||null,body.published_at||null,body.topic||null,body.score||0,body.confidence||'low').run();
    return json({ok:true},201);
  },
  async scheduled(event, env, ctx) { console.log('scheduled radar run', event.scheduledTime); }
};
