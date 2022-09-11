// dialogs 
import React from 'react';
import L from 'leaflet';
import "leaflet/dist/leaflet.css";
import useGeoData from '../../hooks/useMap/useGeoData';
import { ShowPopupContext } from '../../App';
///
import RooftopDialog from './RooftopDialog';
import PowerstationDialog from './PowerstationDialog';
import FieldDialog from './FieldDialog';
import PvDialog from './PvDialog';


export default function useLayers() {
    const getGeoData = useGeoData()
    const { updatePopup } = React.useContext(ShowPopupContext)

    const addRooftops = (mini_map) => {
        const data = getGeoData('/api/rooftops', {})
        data.then((res) => {
            const roofs = L.geoJSON(res, {
                onEachFeature: (feature, layer) => {
                    const style = layer.setStyle({
                        "color": "red",
                        "weight": 5,
                        "opacity": 0.65
                    })
                    const click = layer.on('click', async function (e) {
                        updatePopup({ open: true, content: <RooftopDialog data={feature} /> })
                    })

                }
            }
            );
            mini_map.addLayer(roofs)
        })
    }

    const addPowerplants = (mini_map) => {
        const powerstations = getGeoData('/api/get-powerstations', {})
        powerstations.then((res) => {

            const power = L.geoJSON(res, {
                onEachFeature: (feature, layer) => {
                    const style = layer.setStyle({
                        "color": "red",
                        "weight": 5,
                        "opacity": 0.65
                    })
                    const click = layer.on('click', async function (e) {
                        updatePopup({ open: true, content: <PowerstationDialog data={feature} /> })
                    })

                }
            }
            );
            mini_map.addLayer(power)
        })
    }

    const addPv = (mini_map) => {
        const pv = getGeoData('/api/get-pv', {})
        pv.then((res) => {
            const _pv = L.geoJSON(res, {
                onEachFeature: (feature, layer) => {
                    const style = layer.setStyle({
                        "color": "#0ca635",
                        "weight": 5,
                        "opacity": 0.65
                    })
                    const click = layer.on('click', async function (e) {
                        updatePopup({ open: true, content: <PvDialog data={feature} /> })
                    })

                }
            }
            );
            mini_map.addLayer(_pv)
        })
    }

    const addFields = (mini_map) => {
        const field = getGeoData('/api/get-field', {})
        field.then((res) => {
            const _field = L.geoJSON(res, {
                onEachFeature: (feature, layer) => {
                    const style = layer.setStyle({
                        "color": "#084a1a",
                        "weight": 5,
                        "opacity": 0.65
                    })
                    const click = layer.on('click', async function (e) {
                        updatePopup({ open: true, content: <FieldDialog data={feature} /> })
                    })

                }
            }
            );
            mini_map.addLayer(_field)
        })
    }


    const loadAll = (mapObject) => {
        try {
            addRooftops(mapObject)
            addPowerplants(mapObject)
            addPv(mapObject)
            addFields(mapObject)
        }
        catch (e) {
            console.log(e)
        }
    }



    return loadAll
}
