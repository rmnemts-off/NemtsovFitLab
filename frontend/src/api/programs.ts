import apiClient from './client'

export interface Program {
  id: number
  name: string
  description: string
  price: number | null
  duration_weeks: number | null
}

export async function getPrograms(): Promise<Program[]> {
  const res = await apiClient.get<Program[]>('/programs/')
  return res.data
}
