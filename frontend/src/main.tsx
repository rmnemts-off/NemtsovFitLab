import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { init, isTMA } from '@telegram-apps/sdk-react'
import App from './App'

if (isTMA()) {
  init()
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
