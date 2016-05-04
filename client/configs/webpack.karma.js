var webpack = require('webpack');
var clientConfig = require('./webpack.client.js');

clientConfig.module.preLoaders = [

  // Transpile only tests
  {
    test: /\.spec\.jsx?/,
    loader: 'babel',
    exclude: /node_modules/,
  },

  // Transpile all project without tests and index.js
  {
    test: /\.jsx?$/,
    exclude: [
      /node_modules/,
      /\.spec\.jsx?/,
    ],
    loader: 'isparta',
  },
];

clientConfig.externals = {
  jsdom: 'window',
  cheerio: 'window',
  'react/lib/ExecutionEnvironment': true,
  'react/lib/ReactContext': 'window',
  'text-encoding': 'window',
};

clientConfig.isparta = {
  embedSource: true,
  noAutoWrap: true,

  // These babel options will be passed only to isparta and not to babel-loader
  babel: {
    presets: ['es2015', 'stage-0', 'react'],
  },
};

module.exports = clientConfig;
