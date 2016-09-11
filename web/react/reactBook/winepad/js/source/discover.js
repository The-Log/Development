'use strict';
import Button from './components/Button';
import Logo from './components/Logo';
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  <div style={ {padding: '20px'} }>
    <h1>Component discoverer </h1>
    <h2>Logo</h2>
    <div style={ {display: 'inline-block', background: 'purple'} }>
      <Logo />
      {/* more components go here... */}
      <div>Button with onClick: <Button onClick={() => alert('ouch')}>Click me</Button></div>
      <div>A link: <Button href="tooedgyfor.me">Follow me</Button></div>
      <div>Custom class name: <Button className="custom">I do nothing</Button></div>
    </div>,
  </div>
  document.getElementById('pad')
);
