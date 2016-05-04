import React from 'react';
import classNames from 'classnames';
import FlatBlockCommonComponent from './common-component';

export default React.createClass({
  displayName: 'FlatBlockBackgroundImage',

  propTypes: {
    src: React.PropTypes.string.isRequired,
  },

  renderValue({ fileUrl }) {
    return (
      <div {...this.props}
        style={{ backgroundImage: `url(${fileUrl || file})` }}></div>
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
