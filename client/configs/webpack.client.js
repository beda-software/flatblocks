var _ = require('lodash');
var webpack = require('webpack');
var path = require('path');
var commonConfig = require('./webpack.common.js');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');
var nested = require('postcss-nested');
var csso = require('postcss-csso');

var clientConfig = _.merge({}, commonConfig, {
  target: 'web',
  devtool: false,
  entry: [
    'babel-polyfill',
    '../src/client',
  ],
  output: {
    path: path.join(__dirname, '../static/dist'),
    filename: 'client.js',
    chunkFilename: '[name].[id].js',
  },
  plugins: [
    new ExtractTextPlugin('client.css', { allChunks: true }),
    new webpack.DefinePlugin({
      __CLIENT__: true,
      __SERVER__: false,
      __PRODUCTION__: true,
      __DEV__: false,
    }),
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurenceOrderPlugin(),

    new webpack.optimize.UglifyJsPlugin({ compress: { warnings: false } }),
  ],
  postcss: function () {
    return [
      nested,
      autoprefixer,
      csso,
    ];
  },
});

clientConfig.module.loaders.push({
  test: /\.css/,
  loader: ExtractTextPlugin.extract('style', [
    'css?modules&importLoaders=1&localIdentName=[hash:base64:6]',
    'postcss'
  ]),
});

module.exports = clientConfig;
