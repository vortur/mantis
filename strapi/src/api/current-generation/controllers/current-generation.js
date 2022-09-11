'use strict';

/**
 * current-generation controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::current-generation.current-generation');
