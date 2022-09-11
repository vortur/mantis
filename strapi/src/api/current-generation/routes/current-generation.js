'use strict';

/**
 * current-generation router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::current-generation.current-generation');
