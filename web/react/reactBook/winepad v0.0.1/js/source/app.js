'use strict';
import Excel from './components/Excel';
import Logo from './components/Logo';
import React from 'react';
import ReactDOM from 'react-dom';

var headers = localStorage.getItem('headers');
var data = localStorage.getItem('data');

if (!headers) {
  headers = ['Title', 'Year', 'Rating', 'Comments'];
  data = [['meme', '2015', 'shit', 'gay'],['meme 2', '2016', 'shit', 'homo'],['meme rebirth', '2017', 'shit', 'fuck']];
}

ReactDOM.render(
  <div>
    <h1>
      <Logo/> Welcome to The App!
    </h1>
    <Excel headers={headers} initialData={data} />
  </div>,
  document.getElementById('pad')
);
