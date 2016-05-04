const nconf = require('nconf');
const path = require('path');

nconf
  .file({
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
