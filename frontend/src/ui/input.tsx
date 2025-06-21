import { InputHTMLAttributes } from 'react';

export function Input(props: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      {...props}
      className={`border rounded px-3 py-2 w-full ${props.className || ''}`}
    />
  );
}
