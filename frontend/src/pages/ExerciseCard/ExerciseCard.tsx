import { useEffect, useState } from 'react'
import { useNavigate, useParams, useLocation } from 'react-router-dom'
import { useBackButton } from '@telegram-apps/sdk-react'
import { getExerciseById, type Exercise } from '../../api/exercises'
import styles from './ExerciseCard.module.css'

interface LocationState {
  sets?: number
  reps?: string
  from?: string
}

export default function ExerciseCard() {
  const { exerciseId } = useParams<{ exerciseId: string }>()
  const navigate = useNavigate()
  const location = useLocation()
  const state = (location.state ?? {}) as LocationState

  const [exercise, setExercise] = useState<Exercise | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  const backButton = useBackButton()

  useEffect(() => {
    let cleanup: (() => void) | undefined
    try {
      backButton.show()
      const off = backButton.on('click', () => navigate(-1))
      cleanup = () => {
        off()
        backButton.hide()
      }
    } catch {
      // not inside Telegram, dev mode
    }
    return cleanup
  }, [backButton, navigate])

  useEffect(() => {
    if (!exerciseId) return
    getExerciseById(exerciseId)
      .then(setExercise)
      .catch(() => setError(true))
      .finally(() => setLoading(false))
  }, [exerciseId])

  if (loading) {
    return (
      <div className={styles.page}>
        <div className={styles.videoPlaceholder}>Загрузка...</div>
      </div>
    )
  }

  if (error || !exercise) {
    return <p className={styles.errorText}>Упражнение не найдено.</p>
  }

  return (
    <div className={styles.page}>
      <div className={styles.videoWrapper}>
        {exercise.video_file_id ? (
          // TODO: video_file_id хранится в Telegram — необходимо разрешить через backend API для получения реального URL
          <video
            className={styles.video}
            controls
            playsInline
            src={`/api/v1/files/${exercise.video_file_id}`}
          />
        ) : (
          <div className={styles.videoPlaceholder}>Видео недоступно</div>
        )}
      </div>

      <div className={styles.body}>
        <div className={styles.muscleTag}>{exercise.muscle_group}</div>
        <h1 className={styles.title}>{exercise.name}</h1>

        {(state.sets !== undefined || state.reps !== undefined) && (
          <div className={styles.setsInfo}>
            {state.sets !== undefined && (
              <div className={styles.stat}>
                <div className={styles.statValue}>{state.sets}</div>
                <div className={styles.statLabel}>Подходов</div>
              </div>
            )}
            {state.reps !== undefined && (
              <div className={styles.stat}>
                <div className={styles.statValue}>{state.reps}</div>
                <div className={styles.statLabel}>Повторений</div>
              </div>
            )}
          </div>
        )}

        {exercise.description && (
          <>
            <div className={styles.divider} />
            <div className={styles.descriptionLabel}>Описание</div>
            <p className={styles.description}>{exercise.description}</p>
          </>
        )}
      </div>
    </div>
  )
}
