import { Box } from '@mui/material'
import React from 'react'
import { Link } from 'react-router-dom'
import FormWrapper from '../../../components/FormWrapper'
import ROUTES from '../../constants/routes'
import ReplaceForm from './ReplaceForm'

const Replace = () => {
  return (
    <Box
      height='100%'
      display='flex'
      flexDirection='column'
      justifyContent='center'
    >
      <Box display='flex' justifyContent='center' mt={8}>
        <Link to={ROUTES.MATCH} style={{ fontSize: 34 }}>
          Match
        </Link>
      </Box>

      <FormWrapper>
        <ReplaceForm />
      </FormWrapper>
    </Box>
  )
}

export default Replace
