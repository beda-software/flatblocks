var _ = require('lodash');
var webpack = require('webpack');
var path = require('path');
var PolyfillsPlugin = require('webpack-polyfills-plugin');
var commonConfig = require('./webpack.common.js');

module.exports = _.merge({}, commonConfig, {
  target: 'web',
  devtool: false,
  entry: ['../src/client'],
  output: {
    path: path.join(__dirname, '../static/dist'),
    publicPath: '/dist',
    filename: 'client.js',
    chunkFilename: '[name].[id].js',
  },
  plugins: [
    new webpack.ProvidePlugin({
      _: 'lodash',
    }),
    new webpack.DefinePlugin({
      __CLIENT__: true,
      __SERVER__: false,
      __PRODUCTION__: true,
      __DEV__: false,
    }),
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({ compress: { warnings: false } }),
    new PolyfillsPlugin([
      '_enqueueMicrotask',
      'Promise',
      'String/prototype/startsWith',
    ]),
  ],
});
