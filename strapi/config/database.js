const path = require('path');

module.exports = ({ env }) => ({
  connection: {
    client: 'mysql',
    pool: {
      "min": 0,
      "max": 7,
    },
    connection: {
      host: env('DATABASE_HOST', '127.0.0.1'),
      port: env.int('DATABASE_PORT', 3306),
      database: env('DATABASE_NAME', 'strapi'),
      user: env('DATABASE_USERNAME', 'strapi'),
      password: env('DATABASE_PASSWORD', 'strapi'),
      ssl: false,
    },
    debug: false,
  },
});
