import React,{ useState, useEffect } from "react";
import useConfirmConnections from "./useConfirmConnections";
import useAxios from "../axios/useAxios";
import * as L from 'leaflet';
import useGeoData from "./useGeoData";

export default function useRooftops() {

    const url = '/api/rooftops'
    const [ rooftopLayerGeoJson, setRooftopLayerGeoJson ] = useState(null)
    const params = {
        typeName: 'osm:dachy_domy',
        maxFeatures: 3000,
    }
 
    const getGeoData = useGeoData(params)

    useEffect(() => {
        const data = getGeoData(url,params)
        setRooftopLayerGeoJson(data)
    }, [])
    
    const returnRoofTops = () => {
        let roofs = {}
        try{
            roofs = L.geoJSON(rooftopLayerGeoJson);
        }
        catch(e){
            console.log(e)
        }
        return roofs
    }
    
  
    return { returnRoofTops }
}