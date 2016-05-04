import React from 'react';
import FirstFlatBlock from './components/first-flatblock';
import SecondFlatBlock from './components/second-flatblock';

export default React.createClass({
  displayName: 'Main',

  render() {
    return (
      <div className="row">
        <div className="col-lg-6">
          <FirstFlatBlock />
        </div>
        <div className="col-lg-6">
          <SecondFlatBlock />
        </div>
      </div>
    );
  },
});
