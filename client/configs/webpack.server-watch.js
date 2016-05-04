var webpack = require('webpack');
var serverConfig = require('./webpack.server.js');
var config = require('./config');

var wdsHost = config.get('FRONTEND_DEV_HOST');
var wdsPort = config.get('FRONTEND_DEV_PORT');

serverConfig.cache = true;
serverConfig.debug = true;

serverConfig.entry.unshift(
  'webpack/hot/poll?1000'
);

serverConfig.output.publicPath = 'http://' + wdsHost + ':' + wdsPort + '/dist';

serverConfig.plugins = [
  new webpack.ProvidePlugin({
    _: 'lodash',
  }),
  new webpack.DefinePlugin({
    __CLIENT__: false,
    __SERVER__: true,
    __PRODUCTION__: false,
    __DEV__: true,
  }),
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
];

module.exports = serverConfig;
