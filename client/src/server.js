import babelPolyfill from 'babel-polyfill';
import Koa from 'koa';
import koaProxy from 'koa-proxy';
import koaStatic from 'koa-static';
import convert from 'koa-convert';

import React from 'react';
import ReactDOM from 'react-dom/server';
import { match as routerMatch, RouterContext } from 'react-router';
import { renderToString } from 'baobab-react-resolver';
import initialRoutes from 'js/routes/route';
import config from '../configs/config';
import RedBox from 'redbox-react';

function match(options) {
  return new Promise((resolve, reject) => {
    routerMatch(options, (error, redirectLocation, renderProps) => {
      if (error || !renderProps) {
        reject(error);
      } else {
        resolve([redirectLocation, renderProps]);
      }
    });
  });
}

try {
  let routes = initialRoutes;

  const app = new Koa();
  app.use(convert(koaStatic('static')));
  app.use(async(ctx, next) => {
    const wdsHost = config.get('FRONTEND_DEV_HOST');
    const wdsPort = config.get('FRONTEND_DEV_PORT');
    const webserver = __PRODUCTION__ ? '' : `//${wdsHost}:${wdsPort}`;
    const location = ctx.path;

    try {
      const [redirectLocation, renderProps] = await match({ routes, location });

      if (redirectLocation) {
        ctx.redirect(redirectLocation.pathname + redirectLocation.search, '/');
        return;
      }

      const { reactString, initialTree } = await renderToString(
        <RouterContext {...renderProps} />);

      const styleAsset = __PRODUCTION__ ?
        `<link rel='stylesheet' href='${webserver + '/dist/client.css'}'>` : ``;

      ctx.type = 'text/html';
      ctx.body = (
        `<!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <title>Stub Project</title>
            ${styleAsset}
          </head>
          <body>
            <div id="react-root">${reactString}</div>
          </body>
          <script>
            window.__TREE__ = ${JSON.stringify(initialTree)};
          </script>
          <script src='${webserver + '/dist/client.js'}'></script>
        </html>`
      );
    } catch (error) {
      ctx.type = 'text/html';

      if (error && error.stack) {
        ctx.status = 500;
        ctx.body = ReactDOM.renderToStaticMarkup(<RedBox error={error} />);
      } else {
        ctx.status = 404;
        ctx.body = 'Requested url not found';
      }
    }

    await next();
  });

  const serverHost = '0.0.0.0';
  const serverPort = config.get('PORT');

  app.listen(serverPort, () => {
    console.info('==> ✅  Server is listening');
    console.info('==> 🌎  Go to http://%s:%s', serverHost, serverPort);
  });

  if (__DEV__) {
    if (module.hot) {
      console.log('[HMR] Waiting for server-side updates');

      module.hot.accept('js/routes/route', () => {
        routes = require('js/routes/route').default;
      });

      module.hot.addStatusHandler((status) => {
        if (status === 'abort') {
          setTimeout(() => process.exit(0), 0);
        }
      });
    }
  }
}
catch (error) {
  console.error(error.stack || error);
}
