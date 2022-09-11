import React, { useState, useEffect } from 'react';
import { Container } from '@mui/system';
import { Switch, FormControl } from '@mui/material';
//
import L from 'leaflet';
import "leaflet/dist/leaflet.css";
// CUSTOM HOOKS
import useTileLayer from '../../hooks/useMap/useTileLayer';
import useLayers from './utility';
import Bar from '../../components/Bar';

const MainPage = () => {
    const ref = React.useRef()
    const loadAll = useLayers()
    const createLayer = useTileLayer()

    useEffect(() => {
        let mini_map = L.map(ref.current, { center: [49.815094, 19.046327], zoom: 16, preferCanvas: true })
        let layer_names = [
            'osm:osm_defaults', 'osm:osm1', 'osm:osm2',
        ]
        const tile_layers = layer_names.map((layer) => {
            return createLayer(layer)
        })

        if (!window.localStorage.getItem('current_map')) window.localStorage.setItem('current_map', 0)
        let current_map = window.localStorage.getItem('current_map')
        try {
            loadAll(mini_map);
            tile_layers[current_map].addTo(mini_map)
        }
        catch (e) {
            console.log(e)
        }

        return () => {
            mini_map.off();
            mini_map.remove();
        }

    }, [])



    return (
        <>
            <Bar />
            <Container sx={{ pt: '15px' }} maxWidth >
                <div ref={ref} style={{ margin: '5px', height: '90vh', width: 'auto' }} ></div>
            </Container>
        </>

    )
}

export default React.memo(MainPage)