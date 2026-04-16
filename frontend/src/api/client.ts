import axios from 'axios'
import { retrieveLaunchParams } from '@telegram-apps/sdk-react'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? '/api/v1',
})

apiClient.interceptors.request.use((config) => {
  try {
    const { initDataRaw } = retrieveLaunchParams()
    if (initDataRaw) {
      config.headers.Authorization = `tma ${initDataRaw}`
    }
  } catch {
    // not inside Telegram, dev mode
  }
  return config
})

export default apiClient
