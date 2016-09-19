var webpack = require('webpack');
var path = require('path');

module.exports = {
  cache: false,
  context: __dirname,
  debug: false,
  module: {
    loaders: [
      {
        test: /\.json$/,
        loaders: ['json'],
      },
      {
        test: /\.(ico|gif|png|jpg|jpeg|webp)$/,
        loaders: ['file?context=static&name=/[path][name].[ext]'],
        exclude: /node_modules/,
      },
      {
        test: /\.(eot|woff|woff2|svg|ttf)$/,
        loader: 'url?limit=50000&name=/[name].[ext]',
      },
    ],
    postLoaders: [
      {
        test: /\.js$/,
        loaders: ['babel?presets[]=es2015&presets[]=stage-0&presets[]=react'],
        exclude: /node_modules/,
      },
    ],
    noParse: /\.min\.js/,
  },
  resolve: {
    modulesDirectories: [
      'src',
      'node_modules',
      'static',
    ],
    alias: {
      api: path.resolve('./src/js/api/'),
      components: path.resolve('./src/js/components/'),
    },
    extensions: ['', '.json', '.js', '.css'],
  },
  node: {
    __dirname: true,
    fs: 'empty',
  },
};
