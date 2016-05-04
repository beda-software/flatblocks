import React from 'react';
import { FlatBlock, FlatBlockImage, FlatBlockComponent } from 'components/flatblocks';

export default React.createClass({
  render() {
    return (
      <FlatBlock slug="example.first">
        <div className="jumbotron">
          <h1>
            <FlatBlockComponent field="header">
              Example 1
            </FlatBlockComponent>
          </h1>
          <FlatBlockComponent field="content">
            This is simple example
          </FlatBlockComponent>
          <FlatBlockImage
            style={{ width: 250 }}
            src="http://static8.depositphotos.com/1003153/893/v/950/depositphotos_8938809-Example-rubber-stamp.jpg" />
        </div>
      </FlatBlock>
    );
  },
});
