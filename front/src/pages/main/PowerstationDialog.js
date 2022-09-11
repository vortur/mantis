import React from 'react'
import { DialogContent, DialogTitle, Stack, Paper } from '@mui/material'

const PowerstationDialog = ({data}) => {
  return (
    <>
      <DialogTitle component={Paper} elevation={3} >
        {'Dane elektrowni'}
      </DialogTitle>
      <DialogContent>
        <Stack>
        <div>{data && `Nazwa: ${data.properties.name}`}</div>
        <div>{data && `Zarządca: ${data?.properties?.operator}`}</div>
        <div>{data && `Moc: ${data?.properties?.['plant:output:electricity']}`}</div>
        </Stack>
      </DialogContent>
    </>
  )
}

export default PowerstationDialog