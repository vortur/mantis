import useConfirmConnections from "./useConfirmConnections";
import useAxios from "../axios/useAxios";
import * as L from 'leaflet';
import 'leaflet-wms-header';

export default function useTileLayer() {
    const { confirmConnections, geoserver_url } = useConfirmConnections();
    const { plainBearerHeader } = useAxios()

    const createLayer = (layer) => {
        if(true) {
            const tiles = L.TileLayer.wmsHeader(
                "/api/geoserver", 
            {
                layers: layer,
                format: 'image/png',
                transparent: true,
                version: '1.3.0',
                crs: L.CRS.EPSG3857,
                query_layers: layer,
                tiled: true,
                info_format: 'text/html',
            },
            [
                { header: 'Authorization', value: plainBearerHeader() },
            ],
            )
            return tiles
        }

    }
    return createLayer

}