import React from 'react';
import FlatBlockCommonComponent from './common-component';
import _ from 'lodash';

export default React.createClass({
  displayName: 'FlatBlockComponent',

  propTypes: {
    field: React.PropTypes.string.isRequired,
  },

  renderValue(values) {
    return (
      <div {..._.omit(this.props, 'children')}
        dangerouslySetInnerHTML={{ __html: values[this.props.field] }}></div>
    );
  },

  render(values) {
    return (
      <FlatBlockCommonComponent
        defaultValues={{ [this.props.field]: this.props.children }}
        render={this.renderValue} />
    );
  },
});

