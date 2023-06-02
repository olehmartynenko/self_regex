import { Box } from '@mui/material'
import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import FormWrapper from '../../../components/FormWrapper'
import ROUTES from '../../constants/routes'
import ReplaceForm from './ReplaceForm'
import Result from './Result'

const Replace = () => {
  const [resultText, setResultText] = useState('')
  const [step, setStep] = useState(0)

  const getStep = () => {
    switch (step) {
      case 0:
        return <ReplaceForm setResultText={setResultText} setStep={setStep} />
      case 1:
        return (
          <Result
            handleBack={() => {
              setStep(0)
              setResultText('')
            }}
            text={resultText}
          />
        )
      default:
        return <ReplaceForm setResultText={setResultText} setStep={setStep} />
    }
  }

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

      <FormWrapper>{getStep()}</FormWrapper>
    </Box>
  )
}

export default Replace
