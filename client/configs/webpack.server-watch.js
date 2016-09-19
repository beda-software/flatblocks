var webpack = require('webpack');
var nodeExternals = require('webpack-node-externals');
var commonConfig = require('./webpack.common.js');
var config = require('./config');
var _ = require('lodash');
var nested = require('postcss-nested');
var path = require('path');

var wdsHost = config.get('FRONTEND_DEV_HOST');
var wdsPort = config.get('FRONTEND_DEV_PORT');

var serverConfig = _.merge({}, commonConfig, {
  target: 'node',
  cache: true,
  debug: true,
  devtool: 'source-map',
  entry: [
    'webpack/hot/poll?1000',
    '../src/server',
  ],
  output: {
    path: path.join(__dirname, '../dist'),
    publicPath: 'http://' + wdsHost + ':' + wdsPort + '/dist',
    filename: 'server.js',
  },
  watchOptions: {
    poll: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      __CLIENT__: false,
      __SERVER__: true,
      __PRODUCTION__: false,
      __DEV__: true,
    }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
  ],
  externals: [
    nodeExternals({
      whitelist: ['webpack/hot/poll?1000'],
    }),
  ],
  postcss: function () {
    return [
      nested,
    ];
  },
});

serverConfig.module.loaders.push({
  test: /\.css/,
  loaders: [
    'fake-style',
    'css?modules&importLoaders=1&localIdentName=[name]___[local]---[hash:base64:3]',
    'postcss',
  ],
});

module.exports = serverConfig;
