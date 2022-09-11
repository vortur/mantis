import React from 'react'
import { DialogContent, DialogTitle, Stack, Paper } from '@mui/material'

const PvDialog = ({ data }) => {

  return (
    <>
      <DialogTitle component={Paper} elevation={3} >
        {'Dane instalacji fotowoltaicznej'}
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

export default PvDialog