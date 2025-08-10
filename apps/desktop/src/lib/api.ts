export const API_BASE = process.env.VITE_API_BASE || 'http://localhost:8000/v1'

export async function prime(query: string, k = 12, entropy = 0) {
  const res = await fetch(`${API_BASE}/prime`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, k, entropy })
  })
  return res.json()
}