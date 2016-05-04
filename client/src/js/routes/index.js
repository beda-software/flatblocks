import React from 'react';
import { SchemaBranchMixin } from 'baobab-react-mixins';
import { ResolveMixin } from 'baobab-resolver';
import flatBlocksApi from 'api/flatblocks';
import { DevToolbar } from 'components';

export default React.createClass({
  displayName: 'BaseApp',

  mixins: [SchemaBranchMixin, ResolveMixin],

  cursors: {
    flatBlocks: ['flatBlocks'],
  },

  getResolve() {
    return [
      {
        cursor: this.cursors.flatBlocks,
        getPromise: flatBlocksApi.getList,
      },
    ];
  },

  render() {
    if (!this.isFullyLoaded()) {
      return <div>
        Preloader...
      </div>;
    }

    return (
      <div className="container">
        <div className="header clearfix">
          <h3 className="text-muted">FlatBlocks</h3>
        </div>
        {__DEV__ ? <DevToolbar /> : null}
        {this.props.children}
      </div>
    );
  },
});
