import styles from './Skeleton.module.css'

interface SkeletonRowsProps {
  count?: number
}

export function SkeletonRows({ count = 3 }: SkeletonRowsProps) {
  return (
    <>
      {Array.from({ length: count }).map((_item, i) => (
        <div key={i} className={styles.row}>
          <div className={`${styles.block} ${styles.orderBlock}`} />
          <div className={styles.fill}>
            <div className={`${styles.block} ${styles.nameBlock}`} />
            <div className={`${styles.block} ${styles.metaBlock}`} />
          </div>
        </div>
      ))}
    </>
  )
}
