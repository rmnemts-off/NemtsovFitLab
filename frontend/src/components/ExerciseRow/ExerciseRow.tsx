import styles from './ExerciseRow.module.css'

interface ExerciseRowProps {
  order?: number
  name: string
  sets?: number
  reps?: string
  onClick: () => void
}

export default function ExerciseRow({ order, name, sets, reps, onClick }: ExerciseRowProps) {
  const meta = sets && reps ? `${sets} × ${reps}` : null

  return (
    <button className={styles.row} onClick={onClick}>
      {order !== undefined && (
        <span className={styles.order}>{order}</span>
      )}
      <div className={styles.info}>
        <div className={styles.name}>{name}</div>
        {meta && <div className={styles.meta}>{meta}</div>}
      </div>
      <span className={styles.arrow}>›</span>
    </button>
  )
}
