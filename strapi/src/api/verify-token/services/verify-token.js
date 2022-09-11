'use strict';

/**
 * verify-token service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::verify-token.verify-token');
