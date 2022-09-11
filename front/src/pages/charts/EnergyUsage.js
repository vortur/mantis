import React, { useState, useEffect } from 'react'
import { Typography, Stack, Skeleton } from '@mui/material'
import { ResponsiveLine } from '@nivo/line'
import useAxios from '../../hooks/axios/useAxios'

const EnergyUsage = () => {

    const { get } = useAxios();
    const [data, setData] = useState(false);

    const getData = async () => {
        const array = []
        const temp = await get('/api/get-energy-usage')
        array.push(temp.data)
        console.log(array)
        setData(temp.data)
    }

    useEffect(() => {
        getData();
    }, [])

    return (

        data ? <Stack>
            <Typography variant='h6' >{'Zużycie energii:'}</Typography>
            <div style={{ height: '500px' }} >
                <ResponsiveLine
                    data={data}
                    margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
                    xScale={{ type: 'point' }}
                    yScale={{
                        type: 'linear',
                        min: 'auto',
                        max: 'auto',
                        stacked: true,
                        reverse: false
                    }}
                    yFormat=" >-.2f"
                    axisTop={null}
                    axisRight={null}
                    axisBottom={null}
                    axisLeft={{
                        orient: 'left',
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'moc [W]',
                        legendOffset: -40,
                        legendPosition: 'middle'
                    }}
                    pointSize={10}
                    pointColor={{ theme: 'background' }}
                    pointBorderWidth={2}
                    pointBorderColor={{ from: 'serieColor' }}
                    pointLabelYOffset={-12}
                    useMesh={true}
                    curve="cardinal"
                    legends={[
                        {
                            anchor: 'bottom-right',
                            direction: 'column',
                            justify: false,
                            translateX: 100,
                            translateY: 0,
                            itemsSpacing: 0,
                            itemDirection: 'left-to-right',
                            itemWidth: 80,
                            itemHeight: 20,
                            itemOpacity: 0.75,
                            symbolSize: 12,
                            symbolShape: 'circle',
                            symbolBorderColor: 'rgba(0, 0, 0, .5)',
                            effects: [
                                {
                                    on: 'hover',
                                    style: {
                                        itemBackground: 'rgba(0, 0, 0, .03)',
                                        itemOpacity: 1
                                    }
                                }
                            ]
                        }
                    ]}
                />
            </div>
        </Stack> :
            <>
                <Skeleton variant="rectangular" width={210} height={60} />
                <Skeleton variant="rectangular" width={210} height={60} />
                <Skeleton variant="rectangular" width={210} height={60} />
                <Skeleton variant="rounded" width={210} height={60} />
            </>

    )
}

export default EnergyUsage