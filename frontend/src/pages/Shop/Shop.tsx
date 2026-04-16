import { useEffect, useState } from 'react'
import { getPrograms, type Program } from '../../api/programs'
import { SkeletonRows } from '../../components/Skeleton/Skeleton'
import ConfirmSheet from './ConfirmSheet'
import styles from './Shop.module.css'

export default function Shop() {
  const [programs, setPrograms] = useState<Program[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  const [selectedProgram, setSelectedProgram] = useState<Program | null>(null)

  useEffect(() => {
    getPrograms()
      .then(setPrograms)
      .catch(() => setError(true))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className={styles.page}>
      <div className={styles.header}>
        <h1 className={styles.pageTitle}>Программы</h1>
      </div>

      {loading && <SkeletonRows count={3} />}
      {error && <p className={styles.errorText}>Ошибка загрузки программ.</p>}

      {!loading && !error && (
        <div className={styles.programList}>
          {programs.map((program) => (
            <div key={program.id} className={styles.programCard}>
              <div className={styles.programName}>{program.name}</div>
              {program.duration_weeks && (
                <div className={styles.programMeta}>{program.duration_weeks} недель</div>
              )}
              {program.description && (
                <p className={styles.programDesc}>{program.description}</p>
              )}
              <button
                className={styles.btnRed}
                onClick={() => setSelectedProgram(program)}
              >
                Подписаться
              </button>
            </div>
          ))}
        </div>
      )}

      {selectedProgram && (
        <ConfirmSheet
          program={selectedProgram}
          onClose={() => setSelectedProgram(null)}
        />
      )}
    </div>
  )
}
