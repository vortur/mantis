import React,{ useState, useEffect } from 'react';
import useAxios from '../axios/useAxios';
/**
 * This hook wil serve to confirm mod_mapserver presence and
 * working connection to geoserver under url set in control pro database
 * also returning geoserver url
 */
export default function  useConfirmConnections(){

    const  { post,get }  = useAxios();
    const [geoserver_url, setGeoserverUrl] = useState(false)
    const [geoserver_conn, setGeoserverConn] = useState(false)

    const _checkGeoserverConnection = async () =>{
        try {
            const check_connection = await get("/api/geoserver")
            if (JSON.parse(check_connection.trim()).connection){
                setGeoserverUrl(JSON.parse(check_connection.trim()).url)
                setGeoserverConn(JSON.parse(check_connection.trim()).connection)
            } 
            else {
                setGeoserverUrl(false)
                setGeoserverConn(false)
            }
        }
        catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        _checkGeoserverConnection()
    }, [])
    

    const confirmConnections = async () => {
        if (geoserver_conn) return true
        else return false
    }

    return { confirmConnections, geoserver_url }

}