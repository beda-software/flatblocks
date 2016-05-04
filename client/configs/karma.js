var path = require('path');
var webpack = require('webpack');
var webpackKarmaConfig = require('./webpack.karma.js');

module.exports = function (config) {
  config.set({
    basePath: '../',
    frameworks: ['phantomjs-shim', 'mocha', 'sinon-chai', 'chai', 'sinon'],
    files: [
      '*/tests.js',
    ],
    preprocessors: {
      '*/tests.js': 'webpack',
    },
    reporters: ['coverage', 'dots'],
    notifyReporter: {
      reportEachFailure: true,
    },
    coverageReporter: {
      reporters: [
        {
          type: 'html',
          dir: path.resolve(__dirname, '../report/coverage/'),
        },
      ],
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['PhantomJS'],
    singleRun: true,
    webpack: webpackKarmaConfig,
    webpackServer: {
      noInfo: true,
    },
  });
};
