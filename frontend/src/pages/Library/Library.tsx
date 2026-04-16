import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { getMuscleGroups, getExercisesByGroup, type MuscleGroup, type Exercise } from '../../api/exercises'
import ExerciseRow from '../../components/ExerciseRow/ExerciseRow'
import { SkeletonRows } from '../../components/Skeleton/Skeleton'
import styles from './Library.module.css'

type View = 'groups' | 'exercises'

export default function Library() {
  const navigate = useNavigate()

  const [view, setView] = useState<View>('groups')
  const [groups, setGroups] = useState<MuscleGroup[]>([])
  const [groupsLoading, setGroupsLoading] = useState(true)
  const [groupsError, setGroupsError] = useState(false)

  const [selectedGroup, setSelectedGroup] = useState<MuscleGroup | null>(null)
  const [exercises, setExercises] = useState<Exercise[]>([])
  const [exercisesLoading, setExercisesLoading] = useState(false)
  const [exercisesError, setExercisesError] = useState(false)

  useEffect(() => {
    getMuscleGroups()
      .then(setGroups)
      .catch(() => setGroupsError(true))
      .finally(() => setGroupsLoading(false))
  }, [])

  const openGroup = (group: MuscleGroup) => {
    setSelectedGroup(group)
    setView('exercises')
    setExercises([])
    setExercisesLoading(true)
    setExercisesError(false)

    getExercisesByGroup(group.id)
      .then(setExercises)
      .catch(() => setExercisesError(true))
      .finally(() => setExercisesLoading(false))
  }

  const goBack = () => {
    setView('groups')
    setSelectedGroup(null)
  }

  if (view === 'groups') {
    return (
      <div className={styles.page}>
        <div className={styles.header}>
          <h1 className={styles.pageTitle}>Библиотека</h1>
        </div>

        {groupsLoading && <SkeletonRows count={6} />}

        {groupsError && (
          <p className={styles.errorText}>Ошибка загрузки групп мышц.</p>
        )}

        {!groupsLoading && !groupsError && (
          <div className={styles.grid}>
            {groups.map((group) => (
              <button
                key={group.id}
                className={styles.groupCard}
                onClick={() => openGroup(group)}
              >
                <span className={styles.groupName}>{group.name}</span>
              </button>
            ))}
          </div>
        )}
      </div>
    )
  }

  return (
    <div className={styles.page}>
      <div className={styles.backRow}>
        <button className={styles.backBtn} onClick={goBack} aria-label="Назад">
          ←
        </button>
        <span className={styles.groupTitle}>{selectedGroup?.name}</span>
      </div>

      <div className={styles.exerciseList}>
        {exercisesLoading && <SkeletonRows count={4} />}

        {exercisesError && (
          <p className={styles.errorText}>Ошибка загрузки упражнений.</p>
        )}

        {!exercisesLoading && !exercisesError && exercises.length === 0 && (
          <p className={styles.emptyText}>Упражнений в этой группе пока нет.</p>
        )}

        {exercises.map((ex) => (
          <ExerciseRow
            key={ex.id}
            name={ex.name}
            onClick={() => navigate(`/exercise/${ex.id}`)}
          />
        ))}
      </div>
    </div>
  )
}
