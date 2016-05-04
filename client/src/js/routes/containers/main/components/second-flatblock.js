import React from 'react';
import { FlatBlock, FlatBlockImage, FlatBlockComponent } from 'components/flatblocks';

export default React.createClass({
  render() {
    return (
      <FlatBlock slug="example.second">
        <div className="jumbotron">
          <h1>
            <FlatBlockComponent field="header">
              Example 2
            </FlatBlockComponent>
          </h1>
          <FlatBlockComponent field="content">
            This is simple example 2
          </FlatBlockComponent>
          <FlatBlockImage style={{ width: 250 }} src="/images/local.png" />
        </div>
      </FlatBlock>
    );
  },
});
