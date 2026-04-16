import apiClient from './client'

export interface MuscleGroup {
  id: number
  name: string
}

export interface Exercise {
  id: number
  name: string
  muscle_group: string
  muscle_group_id: number
  description: string
  video_file_id: string | null
}

export async function getMuscleGroups(): Promise<MuscleGroup[]> {
  const res = await apiClient.get<MuscleGroup[]>('/exercises/muscle-groups')
  return res.data
}

export async function getExercisesByGroup(groupId: number | string): Promise<Exercise[]> {
  const res = await apiClient.get<Exercise[]>(`/exercises/muscle-groups/${groupId}`)
  return res.data
}

export async function getExerciseById(exerciseId: number | string): Promise<Exercise> {
  const res = await apiClient.get<Exercise>(`/exercises/${exerciseId}`)
  return res.data
}
