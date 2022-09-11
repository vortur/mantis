'use strict';

/**
 * rooftops service
 */

module.exports = () => ({
    getLayer: async (ctx) => {
      console.log(ctx)
      const axios = require('axios');
      const data = await axios.get(ctx.request.url)
      return data
      },
});
