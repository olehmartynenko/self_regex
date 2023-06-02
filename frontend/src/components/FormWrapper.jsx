import { Box, Paper } from '@mui/material'
import React from 'react'

const FormWrapper = ({ children }) => {
  return (
    <Box
      display='flex'
      flexDirection='column'
      justifyContent='center'
      width={800}
      margin='auto'
      component={Paper}
      padding={4}
    >
      {children}
    </Box>
  )
}

export default FormWrapper
