import { Button, Stack, TextField, Typography } from '@mui/material'
import { useFormik } from 'formik'
import React from 'react'
import * as yup from 'yup'
import { api } from '../../constants/axios'

const validationSchema = yup.object({
  text: yup.string().required('Text is required'),
  regex: yup.string().required('Regex is required'),
})

const MatchForm = ({ setResultText, setStep }) => {
  const onSubmit = async (values) => {
    
    try {
      const response = await api.post('/match', values)
      setStep(1)
      const matches = response.data.matches
      debugger

      setResultText(matches.join(','))
    } catch (error) {
      alert('Something went wrong')
    }
  }
  const formik = useFormik({
    initialValues: {
      text: '',
      regex: '',
    },
    onSubmit,
    validationSchema,
  })
  const { getFieldProps } = formik

  return (
    <form onSubmit={formik.handleSubmit}>
      <Typography variant='h4'>Match</Typography>
      <Stack mt={4} gap={2}>
        <TextField
          autoComplete='off'
          variant='filled'
          label='Regex'
          {...getFieldProps('regex')}
          error={Boolean(formik.errors.regex) && formik.touched.regex}
          helperText={formik.touched.regex && formik.errors.regex}
        />
        <TextField
          autoComplete='off'
          variant='filled'
          label='Text'
          multiline
          rows={6}
          {...getFieldProps('text')}
          error={Boolean(formik.errors.text) && formik.touched.text}
          helperText={formik.touched.text && formik.errors.text}
        />
        <Button variant='contained' size='large' type='submit'>
          Submit
        </Button>
      </Stack>
    </form>
  )
}

export default MatchForm
