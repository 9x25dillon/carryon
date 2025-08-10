export type MemoryEvent = {
  event_id: string
  ts: string
  type: string
  subject: string
  data: string
  sensitivity: 'low' | 'medium' | 'high'
  consent: string
  hash: string
}

export type PrimerResponse = {
  system: string
  messages: { role: 'user' | 'assistant' | 'system'; content: string }[]
  selected_memories: string[]
}