import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { lazy, Suspense } from 'react'
import Layout from './components/Layout/Layout'

const TodayWorkout = lazy(() => import('./pages/TodayWorkout/TodayWorkout'))
const WorkoutDetail = lazy(() => import('./pages/WorkoutDetail/WorkoutDetail'))
const ExerciseCard = lazy(() => import('./pages/ExerciseCard/ExerciseCard'))
const Library = lazy(() => import('./pages/Library/Library'))
const Shop = lazy(() => import('./pages/Shop/Shop'))

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Suspense fallback={null}>
          <Routes>
            <Route path="/" element={<Navigate to="/workout" replace />} />
            <Route path="/workout" element={<TodayWorkout />} />
            <Route path="/workout/:workoutId" element={<WorkoutDetail />} />
            <Route path="/exercise/:exerciseId" element={<ExerciseCard />} />
            <Route path="/library" element={<Library />} />
            <Route path="/shop" element={<Shop />} />
          </Routes>
        </Suspense>
      </Layout>
    </BrowserRouter>
  )
}
