import React from 'react';
import FlatBlockDevToolbar from './flatblock';

export default React.createClass({
  displayName: 'DevToolbar',

  getInitialState() {
    return {
      show: true,
    };
  },

  onCloseClick() {
    this.setState({
      show: false,
    });
  },

  render() {
    const inlineStyle = {
      position: 'fixed',
      right: 0,
      top: 0,
      zIndex: 1000,
      border: '1px solid black',
      backgroundColor: '#FFF',
      opacity: 0.90,
      width: 130,
      height: 130,
      paddingTop: 5,
      paddingBottom: 5,
      textAlign: 'center',
    };

    if (!this.state.show) {
      return null;
    }

    return (
      <div style={inlineStyle}>
        <b>DevToolbar</b>&nbsp;
        <span onClick={this.onCloseClick}>
          [X]
        </span>
        <hr />
        <div>
          <FlatBlockDevToolbar />
        </div>
      </div>
    );
  },
});
