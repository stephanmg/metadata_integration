import API from '@/services/API'

export default {
  query (queryStringAsJSON) {
    console.log('my query:')
    console.log(queryStringAsJSON)
    return API().post('/query', queryStringAsJSON)
  }
}
