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
        test: /\.(ico|gif|png|jpg|jpeg|svg|webp|eot|woff|ttf)$/,
        loaders: ['file?context=static&name=/[path][name].[ext]'],
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
        loaders: [
          'style-loader',
          'css-loader?minimize',
          'autoprefixer-loader',
          'sass-loader?outputStyle=expanded&includePaths[]=' + (path.resolve(__dirname, './node_modules')),
        ],
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

      // TODO: Use baobab-react-resolver
      'baobab-resolver': path.resolve('./src/js/baobab-resolver/'),
    },
    extensions: ['', '.json', '.js', '.scss'],
  },
  node: {
    __dirname: true,
    fs: 'empty',
  },
};
