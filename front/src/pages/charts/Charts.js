import React, { Suspense } from 'react'
import { Container } from '@mui/system'
import Bar from '../../components/Bar';

const EnergyGeneration = React.lazy(() => import('./EnergyGeneration'));
const EnergyUsage = React.lazy(() => import('./EnergyUsage'));

const Charts = () => {

    return (
        <>
        <Bar />
        <Container >
            
            <Suspense fallback={<div>Wczytywanie...</div>}>
                <EnergyGeneration />
            </Suspense>
            <Suspense fallback={<div>Wczytywanie...</div>}>
                <EnergyUsage />
            </Suspense>

        </Container>
        </>

    )
}

export default Charts