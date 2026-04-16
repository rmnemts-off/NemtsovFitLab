import { type ReactNode } from 'react'
import BottomNav from '../BottomNav/BottomNav'
import styles from './Layout.module.css'

interface LayoutProps {
  children: ReactNode
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div className={styles.layout}>
      <main className={styles.content}>
        {children}
      </main>
      <BottomNav />
    </div>
  )
}
