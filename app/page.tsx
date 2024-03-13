"use client"

import { useState } from 'react';
import useSWR, { mutate } from 'swr';

const fetcher = (url: string) => fetch(url).then(res => res.json());

export default function Mentat() {
  const { data, error } = useSWR('/api/health', fetcher);
  const [postData, setPostData] = useState(null);
  const [inputUrl, setInputUrl] = useState('');

  const sendData = async () => {
    const response = await fetch('/api/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: inputUrl }),
    });
    const newData = await response.json();
    setPostData(newData);
    mutate('/api');
  };

  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <main className="flex flex-col items-center justify-center min-h-screen py-2">
      <h1 className="text-4xl mb-4">Mentat</h1>
      <div className='p-4 flex flex-row gap-12'>
        <div className="flex flex-col items-center">
          <button 
            className="px-4 py-2 mb-4 bg-blue-500 text-white rounded" 
            onClick={() => mutate('/api')}
          >
            Fetch Data
          </button>
          <div className="p-4 bg-gray-800 rounded max-w-32">
            <h2 className="text-2xl mb-2">Received Data:</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </div>
        </div>
        <div className="flex flex-col items-center">
          <input 
            type="text" 
            placeholder="Enter URL" 
            value={inputUrl} 
            onChange={e => setInputUrl(e.target.value)} 
            className="mb-4 px-2 py-1 rounded text-black"
          />
          <button 
            className="px-4 py-2 mb-4 bg-green-500 text-white rounded" 
            onClick={sendData}
          >
            Send Data
          </button>
          <div className="p-4 bg-gray-800 rounded max-w-32">
            <h2 className="text-2xl mb-2">Posted Data:</h2>
            {postData && (
              <pre>{JSON.stringify(postData, null, 2)}</pre>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}