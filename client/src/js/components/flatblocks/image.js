import React from 'react';
import FlatBlockCommonComponent from './common-component';

export default React.createClass({
  displayName: 'FlatBlockImage',

  propTypes: {
    src: React.PropTypes.string.isRequired,
  },

  renderValue({ file, fileUrl }) {
    return (
      <img {...this.props} src={fileUrl || file} />
    );
  },

  render(values) {
    return (
      <FlatBlockCommonComponent
        defaultValues={{ file: this.props.src }}
        render={this.renderValue} />
    );
  },
});
