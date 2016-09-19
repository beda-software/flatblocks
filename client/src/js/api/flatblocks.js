import api from './index';
import _ from 'lodash';

export default {
  getList(cfg) {
    return api.get('/flatblocks/', cfg)
      .then(resp => _.keyBy(resp.data, 'slug'));
  },

  create(data, cfg) {
    return api.post('/flatblocks/', data, cfg)
      .then(resp => resp.data);
  },

  update(data, cfg) {
    return api.patch(`/flatblocks/${data.pk}/`, data, cfg)
      .then(resp => resp.data);
  },
};
