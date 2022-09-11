'use strict';

/**
 * current-usage service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::current-usage.current-usage');
