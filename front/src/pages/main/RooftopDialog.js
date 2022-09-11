import React from 'react'
import { DialogContent, DialogTitle, Stack, Paper } from '@mui/material'


const RooftopDialog = ({ data }) => {

  return (
    <>
      <DialogTitle component={Paper} elevation={3} >
        {'Dane instalacji'}
      </DialogTitle>
      <DialogContent>
        <Stack>
        <div>{data && `Identyfikator: ${data.id}`}</div>
        <div>{data && `Powierzchnia dachu: ${data.properties.area} m2`}</div>
        </Stack>
      </DialogContent>
    </>
  )
}

export default RooftopDialog