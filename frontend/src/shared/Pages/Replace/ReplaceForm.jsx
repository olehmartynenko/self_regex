import { Button, Stack, TextField, Typography } from '@mui/material'
import { useFormik } from 'formik'
import { default as React, useState } from 'react'
import * as yup from 'yup'
import { api } from '../../constants/axios'

const validationSchema = yup.object({
  text: yup.string().required('Text is required'),
  regex: yup.string().required('Regex is required'),
  replace: yup.string().required('Replace is required'),
})

const ReplaceForm = () => {
  const [resultText, setResultText] = useState('')

  const onSubmit = async (values) => {
    try {
      const response = await api.post('/replace', values)
      const matches = response.data.matches

      setResultText(matches.join(','))
    } catch (error) {
      alert('Something went wrong')
    }
  }
  const formik = useFormik({
    initialValues: {
      text: '',
      regex: '',
      replace: '',
    },
    onSubmit,
    validationSchema,
  })
  const { getFieldProps } = formik

  return (
    <form onSubmit={formik.handleSubmit}>
      <Typography variant='h4'>Replace</Typography>
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
          label='Replace'
          {...getFieldProps('replace')}
          error={Boolean(formik.errors.replace) && formik.touched.replace}
          helperText={formik.touched.replace && formik.errors.replace}
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
      {resultText && (
        <Typography
          variant='body1'
          mt={4}
          sx={{
            border: '2px solid #B799FF',
            borderRadius: 4,
            p: 2,
            bgcolor: 'rgba(172, 188, 255, 0.25)',
          }}
        >
          {resultText}
        </Typography>
      )}
    </form>
  )
}

export default ReplaceForm
