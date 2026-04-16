import { useLocation, useNavigate } from 'react-router-dom'
import styles from './BottomNav.module.css'

interface Tab {
  path: string
  label: string
  icon: string
}

const TABS: Tab[] = [
  { path: '/workout', label: 'Тренировка', icon: '🏋' },
  { path: '/library', label: 'Библиотека', icon: '📚' },
  { path: '/shop', label: 'Магазин', icon: '🛒' },
]

export default function BottomNav() {
  const location = useLocation()
  const navigate = useNavigate()

  const isActive = (path: string) => location.pathname === path || (path === '/workout' && location.pathname === '/')

  return (
    <nav className={styles.nav}>
      {TABS.map((tab) => (
        <button
          key={tab.path}
          className={`${styles.tab} ${isActive(tab.path) ? styles.active : ''}`}
          onClick={() => navigate(tab.path)}
          aria-label={tab.label}
        >
          <span className={styles.tabIcon}>{tab.icon}</span>
          <span className={styles.tabLabel}>{tab.label}</span>
        </button>
      ))}
    </nav>
  )
}
