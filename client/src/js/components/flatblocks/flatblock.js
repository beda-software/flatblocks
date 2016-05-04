import React from 'react';
import BaobabPropTypes from 'baobab-prop-types';
import { SchemaBranchMixin } from 'baobab-react-mixins';

export default React.createClass({
  displayName: 'FlatBlock',

  mixins: [SchemaBranchMixin],

  propTypes: {
    slug: React.PropTypes.string.isRequired,
  },

  childContextTypes: {
    flatBlockCursor: BaobabPropTypes.cursor.isRequired,
  },

  cursors(props) {
    return {
      flatBlock: ['flatBlocks', 'data', props.slug],
    };
  },

  getChildContext() {
    return {
      flatBlockCursor: this.cursors.flatBlock,
    };
  },

  componentDidMount() {
    this.cursors.flatBlock.set('slug', this.props.slug);
  },

  render() {
    return (
      <div className={this.props.className}>
        {this.props.children}
      </div>
    );
  },
});
