const nconf = require('nconf');
const path = require('path');

nconf
  .file({
    // TODO: .env file is broken
    // TODO: use environment in docker-compose.override.yml
    file: '.env',
    format: nconf.formats.ini,
  })
  .env()
  .defaults({
    FRONTEND_DEV_HOST: 'localhost',
    FRONTEND_DEV_PORT: 8080,
    PORT: 8000,
  });

module.exports = nconf;
