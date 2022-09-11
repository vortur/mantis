'use strict';

/**
 * A set of functions called "actions" for `geoserver`
 */
//  const mime = require('mime-types')
const fs = require('fs');

module.exports = {
  getGeoserver: async (ctx, next) => {
    try {
      const data = await strapi
        .service("api::geoserver.geoserver")
        .getGeoserver(ctx);
      ctx.set('Content-Type', 'image/png')
      ctx.set('Content-Transfer-Encoding', 'binary')
      ctx.set('Content-Disposition','inline; filename=osm-osm2.png')
      ctx.body = data;
      // ctx.set('Content-Length', data.length)
    } catch (err) {
      ctx.badRequest("Post report  543344controller error", { moreDetails: err });
    }
  }
};
