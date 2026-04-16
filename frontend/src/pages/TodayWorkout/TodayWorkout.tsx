import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { getTodayWorkout, type TodayWorkoutResponse } from '../../api/workouts'
import ExerciseRow from '../../components/ExerciseRow/ExerciseRow'
import { SkeletonRows } from '../../components/Skeleton/Skeleton'
import AudioPlayer from '../../components/AudioPlayer/AudioPlayer'
import styles from './TodayWorkout.module.css'

export default function TodayWorkout() {
  const navigate = useNavigate()
  const [data, setData] = useState<TodayWorkoutResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    getTodayWorkout()
      .then(setData)
      .catch(() => setError(true))
      .finally(() => setLoading(false))
  }, [])

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

  if (error) {
    return <p className={styles.errorText}>Ошибка загрузки. Попробуйте позже.</p>
  }

  if (!data?.has_subscription) {
    return (
      <div className={styles.page}>
        <div className={styles.header}>
          <h1 className={styles.dayLabel}>Тренировка</h1>
        </div>
        <div className={styles.noSubCard}>
          <div className={styles.noSubTitle}>Нет активной подписки</div>
          <p className={styles.noSubText}>Оформите подписку, чтобы получить доступ к тренировкам.</p>
          <button className={styles.btnRed} onClick={() => navigate('/shop')}>
            Перейти в магазин
          </button>
        </div>
      </div>
    )
  }

  const workout = data.workout
  if (!workout) {
    return <p className={styles.errorText}>На сегодня тренировок нет. Отдыхайте!</p>
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
