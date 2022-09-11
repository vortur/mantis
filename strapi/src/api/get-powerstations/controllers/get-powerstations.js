'use strict';

/**
 * A set of functions called "actions" for `get-powerstations`
 */

module.exports = {
  getLayer: async (ctx, next) => {
    try {
      const axios = require('axios');
      const data = await axios.get('http://192.168.10.249:8080/geoserver/osm/ows'
      + "?service=WFS&version=1.0.0&request=GetFeature&typeName=osm:elektrownieBB&maxFeatures=500&outputFormat=application%2Fjson")
      let new_data = data.data
      ctx.body = JSON.stringify(new_data)
    } catch (err) {
      ctx.body = err;
    }
  }
};
