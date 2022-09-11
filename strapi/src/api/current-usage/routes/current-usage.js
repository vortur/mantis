'use strict';

/**
 * current-usage router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::current-usage.current-usage');
