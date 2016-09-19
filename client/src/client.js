import React from 'react';
import { Router, browserHistory } from 'react-router';
import { render } from 'baobab-react-resolver';
import routes from 'js/routes/route';
import './styles/main.css';

/**
 * Fire-up React Router.
 */
const containerElement = window.document.getElementById('react-root');

render(
  <Router routes={routes} history={browserHistory} />,
  containerElement,
  null,
  { immutable: false }
);

/**
 * Detect whether the server-side render has been discarded due to an invalid checksum.
 */
if (__DEV__) {
  if (!containerElement.firstChild || !containerElement.firstChild.attributes ||
      !containerElement.firstChild.attributes['data-react-checksum']) {
    console.error('Server-side React render was discarded. ' +
      'Make sure that your initial render does not contain any client-side code.');
  }
}
