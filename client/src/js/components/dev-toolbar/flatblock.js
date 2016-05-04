import React from 'react';
import { BranchMixin } from 'baobab-react-mixins';
import flatBlocksApi from 'api/flatblocks';

export default React.createClass({
  displayName: 'FlatBlockDevToolbar',

  mixins: [BranchMixin],

  cursors: {
    flatBlocks: ['flatBlocks', 'data'],
  },

  onUploadClick() {
    if (!confirm('Do you really want to override existing flatblocks with new values?')) {
      return;
    }

    _.map(this.state.flatBlocks, (flatBlock, slug) => {
      const flatBlockCursor = this.cursors.flatBlocks.select(slug);
      const method = flatBlock.pk ? flatBlocksApi.update : flatBlocksApi.create;

      method(flatBlock)
        .then((data) => flatBlockCursor.set(data));
    });
  },

  render() {
    return (
      <div>
        <b>FlatBlocks</b>
        <br />
        <button onClick={this.onUploadClick}>
          Upload to server
        </button>
      </div>
    );
  },
});
