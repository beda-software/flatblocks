var webpack = require('webpack');
var clientConfig = require('./webpack.client.js');
var config = require('./config');

var wdsHost = config.get('FRONTEND_DEV_HOST');
var wdsPort = config.get('FRONTEND_DEV_PORT');

clientConfig.cache = true;
clientConfig.debug = true;
clientConfig.devtool = 'cheap-module-eval-source-map';
clientConfig.watchOptions = {
  poll: true,
};

clientConfig.entry.unshift(
  'webpack-dev-server/client?http://' + wdsHost + ':' + wdsPort,
  'webpack/hot/only-dev-server'
);

clientConfig.devServer = {
  publicPath: 'http://' + wdsHost + ':' + wdsPort + '/dist',
  hot: true,
  inline: false,
  lazy: false,
  quiet: true,
  noInfo: true,
  headers: { 'Access-Control-Allow-Origin': '*' },
  stats: { colors: true },
  host: '0.0.0.0',
  port: wdsPort,
};

clientConfig.output.publicPath = clientConfig.devServer.publicPath;
clientConfig.output.hotUpdateMainFilename = 'update/[hash]/update.json';
clientConfig.output.hotUpdateChunkFilename = 'update/[hash]/[id].update.js';

clientConfig.plugins = [
  new webpack.ProvidePlugin({
    _: 'lodash',
  }),
  new webpack.DefinePlugin({
    __CLIENT__: true,
    __SERVER__: false,
    __PRODUCTION__: false,
    __DEV__: true,
  }),
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
];

clientConfig.module.postLoaders = [
  {
    test: /\.js$/,
    loaders: ['babel?cacheDirectory&presets[]=es2015&presets[]=stage-0&presets[]=react&presets[]=react-hmre'],
    exclude: /node_modules/,
  },
];

module.exports = clientConfig;
