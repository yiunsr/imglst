const { defineConfig } = require('@vue/cli-service')

const DEPLOYMENT_PATH = '/static/'

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
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
