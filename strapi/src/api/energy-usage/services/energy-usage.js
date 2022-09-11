'use strict';

/**
 * energy-usage service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::energy-usage.energy-usage');
