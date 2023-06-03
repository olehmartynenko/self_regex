import { Box, Button, Typography } from '@mui/material'
import React from 'react'
import { useNavigate } from 'react-router-dom'
import ROUTES from '../../constants/routes'

const Home = () => {
  const navigate = useNavigate()
  return (
    <Box
      display='flex'
      flexDirection='column'
      alignItems='center'
      justifyContent='center'
      height='100vh'
    >
      <Typography variant='h4'>What would you like to do?</Typography>
      <Box display='flex' mt={6} gap={4}>
        <Button
          onClick={() => navigate(ROUTES.MATCH)}
          variant='contained'
          sx={{ width: 200 }}
          size='large'
        >
          Match
        </Button>
        <Button
          onClick={() => navigate(ROUTES.REPLACE)}
          variant='contained'
          sx={{ width: 200 }}
          size='large'
        >
          Replace
        </Button>
      </Box>
    </Box>
  )
}

export default Home
