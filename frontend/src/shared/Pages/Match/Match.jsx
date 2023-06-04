import { Box } from '@mui/material'
import React from 'react'
import { Link } from 'react-router-dom'
import FormWrapper from '../../../components/FormWrapper'
import ROUTES from '../../constants/routes'
import MatchForm from './MatchForm'

const Match = () => {
  return (
    <Box
      height='100%'
      display='flex'
      flexDirection='column'
      justifyContent='center'
    >
      <Box display='flex' justifyContent='center' mt={8}>
        <Link to={ROUTES.REPLACE} style={{ fontSize: 34 }}>
          Replace
        </Link>
      </Box>

      <FormWrapper>
        <MatchForm />
      </FormWrapper>
    </Box>
  )
}

export default Match
