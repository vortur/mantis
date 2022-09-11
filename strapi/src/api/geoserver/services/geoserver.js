'use strict';

/**
 * geoserver service
 */
const fs = require('fs');
const { pipeline } = require('stream/promises');
const http = require("http");
const request = require('request');

module.exports = () => ({
  getGeoserver: async (ctx) => {
    try {
      const url = ctx.request.url.replace('/api/geoserver', 'http://192.168.10.249:8080/geoserver/wms')
      const axios = require('axios');
      // const res = await axios.get(url)
      const res = request.get(url, function (error, response, body) {
        if (!error && response.statusCode == 200) {
          return response.body
        }
      });
      return res

    } catch (err) {
      console.log(err)
    }
  },

});
