import { useRef, useState } from 'react'
import styles from './AudioPlayer.module.css'

interface AudioPlayerProps {
  // audio_briefing_file_id is a Telegram file_id; actual audio src must be resolved server-side
  // For now we display the player UI with the file_id as a placeholder src
  fileId: string
}

export default function AudioPlayer({ fileId }: AudioPlayerProps) {
  const audioRef = useRef<HTMLAudioElement>(null)
  const [playing, setPlaying] = useState(false)

  const toggle = () => {
    if (!audioRef.current) return
    if (playing) {
      audioRef.current.pause()
      setPlaying(false)
    } else {
      audioRef.current.play().then(() => setPlaying(true)).catch(() => setPlaying(false))
    }
  }

  return (
    <div className={styles.card}>
      {/* TODO: resolve Telegram file_id to a real audio URL via backend */}
      <audio
        ref={audioRef}
        src={`/api/v1/files/${fileId}`}
        onEnded={() => setPlaying(false)}
        preload="none"
      />
      <button className={styles.playBtn} onClick={toggle} aria-label={playing ? 'Пауза' : 'Играть'}>
        {playing ? '⏸' : '▶'}
      </button>
      <div>
        <div className={styles.label}>Брифинг тренера</div>
        <div className={styles.status}>{playing ? 'Воспроизведение...' : 'Нажмите для прослушивания'}</div>
      </div>
    </div>
  )
}
