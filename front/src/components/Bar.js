import React from 'react'
import { AppBar, Button } from '@mui/material'
import { Link } from 'react-router-dom';
import { IconButton, MenuItem, Menu, Stack } from '@mui/material';
import MapIcon from '@mui/icons-material/Map';
import SsidChartIcon from '@mui/icons-material/SsidChart';

const Bar = (props) => {

    const pages = [
        { title: <><MapIcon/>{'  Mapa'}</>, path: '/' },
        { title: <><SsidChartIcon/>{'Statystyki'}</>, path: '/charts' },
      ];
      
      

    const container = {
        'justifyContent': 'center',
        'alignItems': 'center'
    }

    const item = {

    }

    return (
        <AppBar style={{ padding: 10 + 'px', backgroundColor:'#88a891' }} position="static">
            <Stack spacing={2} direction={'row'} style={container}>
            {pages.map((page) => (
                <div style={item} >
                <MenuItem key={page.title} style={{margin: 0, padding: 0}}>
                  <Link to={page.path} style={{textDecoration: 'none'}}>
                    <Button variant={'contained'} style={{ backgroundColor:"#4a7555", minWidth:100, justifyContent: 'center', padding:6}}>{page.title}</Button>
                  </Link>
                </MenuItem>
                </div>
              ))}
            </Stack>
        </AppBar>
    )
}

export default Bar
