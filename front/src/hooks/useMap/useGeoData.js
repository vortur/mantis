import React from "react";
import useConfirmConnections from "./useConfirmConnections";
import useAxios from "../axios/useAxios";
import * as L from 'leaflet';
import 'leaflet-wms-header';

import { MapContainerContext } from "../../pages/main/MainPage";
/**
 * hook for fetching geoJSON features 
 * limited based on bounding boxes
 * 
 */
export default function useGeoData() {

    const { get } = useAxios()



    const getGeoData = async (url,params) => {
        try{
            const get_geodata = await get(url)
        if (get_geodata) return get_geodata.data
        }
        catch(e){
            console.log(e)
        }
        
    }

    return getGeoData
}