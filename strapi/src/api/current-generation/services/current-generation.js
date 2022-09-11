'use strict';

/**
 * current-generation service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::current-generation.current-generation');
