'use strict';

/**
 * verify-token controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::verify-token.verify-token');
