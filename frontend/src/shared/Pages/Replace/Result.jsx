import { Box, Button, Typography } from '@mui/material'
import React from 'react'

const Result = ({ text, handleBack }) => {
  return (
    <Box>
      <Box display='flex' justifyContent='space-between' mb={2}>
        <Typography fontWeight={700} variant='h4'>
          Result
        </Typography>
        <Button
          size='large'
          onClick={handleBack}
          variant='outlined'
          color='secondary'
        >
          Back
        </Button>
      </Box>
      {text ? (
        <Typography>{text}</Typography>
      ) : (
        <Typography mt={12} mb={4} color='text.secondary' textAlign='center'>
          No matches found
        </Typography>
      )}
    </Box>
  )
}

export default Result
