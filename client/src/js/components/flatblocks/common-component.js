import React from 'react';
import ReactDOM from 'react-dom/server';
import BaobabPropTypes from 'baobab-prop-types';

export default React.createClass({
  displayName: 'FlatBlockCommonComponent',

  propTypes: {
    defaultValues: React.PropTypes.object.isRequired,
    render: React.PropTypes.func.isRequired,
  },

  contextTypes: {
    flatBlockCursor: BaobabPropTypes.cursor.isRequired,
  },

  getFieldCursor(field) {
    return this.context.flatBlockCursor.select(field);
  },

  componentDidMount() {
    _.map(this.props.defaultValues, (value, field) => {
      const cursor = this.getFieldCursor(field);

      if (!cursor.get()) {
        if (_.isArray(value)) {
          value = ReactDOM.renderToStaticMarkup(
            <div>{value}</div>
          );
        }

        cursor.set(value);
      }
    });
  },

  render() {
    const cursor = this.context.flatBlockCursor;
    
    return this.props.render(cursor.get() || {}, cursor);
  },
});
