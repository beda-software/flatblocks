var webpack = require('webpack');
var nodeExternals = require('webpack-node-externals');
var path = require('path');
var fs = require('fs');
var commonConfig = require('./webpack.common.js');
var _ = require('lodash');

module.exports = _.merge({}, commonConfig, {
  target: 'node',
  devtool: 'source-map',
  entry: ['../src/server'],
  output: {
    path: path.join(__dirname, '../dist'),
    publicPath: '/dist',
    filename: 'server.js',
  },
  plugins: [
    new webpack.ProvidePlugin({
      _: 'lodash',
    }),
    new webpack.DefinePlugin({
      __CLIENT__: false,
      __SERVER__: true,
      __PRODUCTION__: true,
      __DEV__: false,
    }),
  ],
  externals: [
    nodeExternals({
      whitelist: ['webpack/hot/poll?1000'],
    }),
  ],
});
