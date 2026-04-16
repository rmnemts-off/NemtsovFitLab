import type { Program } from '../../api/programs'
import styles from './Shop.module.css'

interface ConfirmSheetProps {
  program: Program
  onClose: () => void
}

export default function ConfirmSheet({ program, onClose }: ConfirmSheetProps) {
  const handlePay = () => {
    // TODO: integrate payment flow (Telegram Payments API)
    onClose()
  }

  const priceLabel = program.price != null ? `${program.price} ₽ / мес` : '— ₽ / мес'

  return (
    <>
      <div className={styles.overlay} onClick={onClose} />
      <div className={styles.sheet}>
        <div className={styles.sheetTitle}>{program.name}</div>
        <div className={styles.sheetPrice}>{priceLabel}</div>
        <div className={styles.sheetActions}>
          <button className={styles.btnCancel} onClick={onClose}>
            Отмена
          </button>
          <button className={styles.btnPay} onClick={handlePay}>
            Оплатить
          </button>
        </div>
      </div>
    </>
  )
}
