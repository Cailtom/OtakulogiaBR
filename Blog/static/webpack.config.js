const modoDev = process.env.NODE_ENV !== 'production';
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

module.exports = {
  mode: modoDev ? 'development' : 'production',
  entry: './index.js',
  output: {
    filename: "bootstrap-min.js",
    path: __dirname + "/dist",
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'bootstrap-min.css'
    })
  ],
  module: {
    rules: [{
      test: /\.s?[ac]ss$/i,
      use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
    }]
  },
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          format: {
            comments: false,
          },
        },
        extractComments: false,
        parallel: true
      }),
      new CssMinimizerPlugin(),
    ]
  }
}
