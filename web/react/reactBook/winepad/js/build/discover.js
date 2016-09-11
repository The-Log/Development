'use strict';

var _Logo = require('./components/Logo');

var _Logo2 = _interopRequireDefault(_Logo);

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _reactDom = require('react-dom');

var _reactDom2 = _interopRequireDefault(_reactDom);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_reactDom2.default.render(_react2.default.createElement(
  'div',
  { style: { padding: '20px' } },
  _react2.default.createElement(
    'h1',
    null,
    'Component discoverer '
  ),
  _react2.default.createElement(
    'h2',
    null,
    'Logo'
  ),
  _react2.default.createElement(
    'div',
    { style: { display: 'inline-block', background: 'purple' } },
    _react2.default.createElement(_Logo2.default, null)
  )
), document.getElementById('pad'));