import { Box, ThemeProvider } from '@mui/material'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import './App.css'
import Home from './shared/Pages/Home/Home'
import Match from './shared/Pages/Match/Match'
import Replace from './shared/Pages/Replace/Replace'
import ROUTES from './shared/constants/routes'
import { theme } from './shared/themes/theme'

const router = createBrowserRouter([
  {
    path: ROUTES.HOME,
    element: <Home />,
  },
  {
    path: ROUTES.MATCH,
    element: <Match />,
  },
  {
    path: ROUTES.REPLACE,
    element: <Replace />,
  },
])

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Box height='100vh'>
        <RouterProvider router={router} />
      </Box>
    </ThemeProvider>
  )
}

export default App
