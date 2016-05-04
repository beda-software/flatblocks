import axios from 'axios';
import defaultsConfig from 'axios/lib/defaults';
import transformKeys from 'transform-keys';

function transformRequest(data) {
  if (data) {
    data = transformKeys(data, _.snakeCase);
  }

  return data;
}

function transformResponse(data) {
  if (data) {
    data = transformKeys(data, _.camelCase);
  }

  return data;
}

function getDevURL() {
  return __SERVER__ ? 'http://server:8000' : 'http://localhost:8000';
}

function getProductionURL() {
  throw Exception('Set production URL');
}

const baseURL = __PRODUCTION__ ? getProductionURL() : getDevURL();

const api = axios.create({
  baseURL,
  skipUnauthorized: false,
  timeout: 600000,
  headers: {},
  transformRequest: [transformRequest, defaultsConfig.transformRequest[0]],
  transformResponse: [defaultsConfig.transformResponse[0], transformResponse],
});

export default api;
