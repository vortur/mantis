import React from 'react'
import { DialogContent, DialogTitle, Stack, Paper } from '@mui/material'

const FieldDialog = ({ data }) => {

  return (
    <>
      <DialogTitle component={Paper} elevation={3} >
        {'Dane działki'}
      </DialogTitle>
      <DialogContent>
        <Stack>
        <div>{data && `Identyfikator: ${data.id}`}</div>
        <div>{data && `Powierzchnia : ${data.properties.area} m2`}</div>
        </Stack>
      </DialogContent>
    </>
  )
}

export default FieldDialog