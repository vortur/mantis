'use strict';

/**
 * energy-generation service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::energy-generation.energy-generation');
