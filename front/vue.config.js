const { defineConfig } = require('@vue/cli-service')

const DEPLOYMENT_PATH = '/static/'

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    // output 파일에 대해 hash 를 붙인다.
    // configureWebpack: config => {
    //   if (process.env.NODE_ENV === 'production') {
    //     config.output.filename = 'js/[name].[hash].js'
    //     config.output.chunkFilename = 'js/[name].[hash].js'
    //   }
    // },
    proxy: {
      '^/demo/': {
        target: 'http://localhost:8000',
        changeOrigin: true
      },
      '^/static/': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    },
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
  }
})
