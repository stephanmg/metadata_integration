import API from '@/services/API'

export default {
    query(queryStringAsJSON) {
        return API().post("query", queryStringAsJSON)
    }
}