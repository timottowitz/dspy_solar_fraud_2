import { Hono } from 'hono';
import { serve } from '@hono/node-server';
import { spawn } from 'child_process';
import { cors } from 'hono/cors';
import { config } from 'dotenv';

config();

const app = new Hono();
app.use('*', cors());

app.post('/generate', async (c) => {
  const clientData = await c.req.json();
  const python = spawn('python', ['generate.py'], {
    stdio: ['pipe', 'pipe', 'inherit'],
  });
  python.stdin.write(JSON.stringify(clientData));
  python.stdin.end();
  let output = '';
  for await (const chunk of python.stdout) {
    output += chunk;
  }
  const exitCode: number | null = await new Promise((resolve) => {
    python.on('close', (code) => resolve(code));
  });
  if (exitCode && exitCode !== 0) {
    return c.text('Error generating document', 500);
  }
  return c.text(output);
});

const port = Number(process.env.PORT) || 3001;
serve({ fetch: app.fetch, port });
