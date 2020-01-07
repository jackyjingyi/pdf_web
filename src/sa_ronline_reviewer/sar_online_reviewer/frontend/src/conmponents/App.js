import React, { Component } from 'react';
import ReactDom from 'react-dom';

class App extends ComponentP {
    render() {
        return <h1>React APP</h1>
    }
}

ReactDom.render(<App />, document.getElementById('app'));