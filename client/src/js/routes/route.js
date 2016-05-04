import React from 'react';
import Base from './index';
import mainRoute from './containers/main/route';

export default {
  component: Base,

  childRoutes: [
    mainRoute,
  ],
};
