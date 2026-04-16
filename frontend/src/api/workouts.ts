import apiClient from './client'

export interface WorkoutExercise {
  id: number
  order: number
  sets: number
  reps: string
  exercise: {
    id: number
    name: string
    muscle_group: string
    description: string
    video_file_id: string | null
  }
}

export interface Workout {
  id: number
  day_number: number
  title: string
  audio_briefing_file_id: string | null
  exercises: WorkoutExercise[]
}

export interface TodayWorkoutResponse {
  workout: Workout | null
  has_subscription: boolean
}

export async function getTodayWorkout(): Promise<TodayWorkoutResponse> {
  const res = await apiClient.get<TodayWorkoutResponse>('/workouts/today')
  return res.data
}

export async function getWorkoutById(workoutId: number | string): Promise<Workout> {
  const res = await apiClient.get<Workout>(`/workouts/${workoutId}`)
  return res.data
}
