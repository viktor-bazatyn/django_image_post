const path = require('path');

module.exports = {
  entry: './djangogramm/static/djangogramm/script/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'djangogramm/static/djangogramm/js'),
    publicPath: '/static/djangogramm/js/'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  mode: 'development',
};

