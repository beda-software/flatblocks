import React from 'react';
import FlatBlockCommonComponent from './common-component';
import _ from 'lodash';

export default React.createClass({
  displayName: 'FlatBlockGallery',

  renderValue({ images }) {
    if (!images || !images.length) {
      return null;
    }

    return (
      <ul {...this.props}>
        {_.map(images, (image) => (
          <li>
            {image.previewFileUrl}
          </li>
        ))}
      </ul>
    );
  },

  render(values) {
    return (
      <FlatBlockCommonComponent
        defaultValues={{ images: [] }} render={this.renderValue} />
    );
  },
});

