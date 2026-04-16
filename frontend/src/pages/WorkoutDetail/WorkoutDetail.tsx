import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { getWorkoutById, type Workout } from '../../api/workouts'
import ExerciseRow from '../../components/ExerciseRow/ExerciseRow'
import { SkeletonRows } from '../../components/Skeleton/Skeleton'
import AudioPlayer from '../../components/AudioPlayer/AudioPlayer'
import styles from './WorkoutDetail.module.css'

export default function WorkoutDetail() {
  const { workoutId } = useParams<{ workoutId: string }>()
  const navigate = useNavigate()
  const [workout, setWorkout] = useState<Workout | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    if (!workoutId) return
    getWorkoutById(workoutId)
      .then(setWorkout)
      .catch(() => setError(true))
      .finally(() => setLoading(false))
  }, [workoutId])

  if (loading) {
    return (
      <div className={styles.page}>
        <div className={styles.header}>
          <div className={styles.loadingTitle} />
        </div>
        <SkeletonRows count={4} />
      </div>
    )
  }

  if (error || !workout) {
    return <p className={styles.errorText}>Тренировка не найдена.</p>
  }

  return (
    <div className={styles.page}>
      <div className={styles.header}>
        <div className={styles.dayLabel}>День {workout.day_number}</div>
        <div className={styles.workoutTitle}>{workout.title}</div>
      </div>

      {workout.audio_briefing_file_id && (
        <div className={styles.audioSection}>
          <AudioPlayer fileId={workout.audio_briefing_file_id} />
        </div>
      )}

      <p className={styles.sectionLabel}>Упражнения</p>
      <div className={styles.exerciseList}>
        {workout.exercises.map((we) => (
          <ExerciseRow
            key={we.id}
            order={we.order}
            name={we.exercise.name}
            sets={we.sets}
            reps={we.reps}
            onClick={() =>
              navigate(`/exercise/${we.exercise.id}`, {
                state: { sets: we.sets, reps: we.reps, from: 'workout' },
              })
            }
          />
        ))}
      </div>
    </div>
  )
}
