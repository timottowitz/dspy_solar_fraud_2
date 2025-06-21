import { ButtonHTMLAttributes } from 'react';

export function Button(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...props}
      className={`px-3 py-2 rounded bg-black text-white hover:bg-gray-800 ${props.className || ''}`}
    />
  );
}
