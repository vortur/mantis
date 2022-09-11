'use strict';

/**
 * verify-token router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::verify-token.verify-token');
