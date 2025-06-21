import { useState } from 'react';
import { Button } from '../ui/button';
import { Input } from '../ui/input';

export default function Home() {
  const [name, setName] = useState('John Doe');
  const [result, setResult] = useState('');

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ client_name: name }),
    });
    setResult(await res.text());
  }

  return (
    <div className="p-4 max-w-xl mx-auto space-y-4">
      <form onSubmit={handleSubmit} className="space-y-2">
        <Input value={name} onChange={e => setName(e.target.value)} />
        <Button type="submit">Generate</Button>
      </form>
      {result && (
        <pre className="whitespace-pre-wrap border p-2 mt-4">{result}</pre>
      )}
    </div>
  );
}
