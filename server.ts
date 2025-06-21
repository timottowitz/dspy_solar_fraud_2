import { Hono } from 'hono';
import { serve } from '@hono/node-server';
import { spawn } from 'child_process';
import { cors } from 'hono/cors';

const app = new Hono();
app.use('*', cors());

app.post('/generate', async (c) => {
  const clientData = await c.req.json();
  const python = spawn('python', ['generate.py'], { stdio: ['pipe', 'pipe', 'inherit'] });
  python.stdin.write(JSON.stringify(clientData));
  python.stdin.end();
  let output = '';
  for await (const chunk of python.stdout) {
    output += chunk;
  }
  return c.text(output);
});

serve({ fetch: app.fetch, port: 3001 });
