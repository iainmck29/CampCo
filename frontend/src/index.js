import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Auth0Provider } from "@auth0/auth0-react"

ReactDOM.render(
  <Auth0Provider
    domain="fsnd-29.eu.auth0.com"
    clientId="afB8Jmjp0gQOgUfS9NNhz8kggCNDe2QX"
    redirectUri="http://localhost:3000"
  >
    <App />
  </Auth0Provider>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
