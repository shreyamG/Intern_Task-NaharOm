import React from "react";
import "./header.css";
// import logo from "./nahar_logo.png";



export default function Header() {
  return (
    <header className="header-fixed">
      <div className="header-limiter">
        <img src="/staticfiles/images/nahar_logo.a2907fa30de71890d83e.png" alt="Logo" id="Logo-Header" />

        <nav id="header-nav">
          <a href="/" id="dlt-sm">
            Home
          </a>
          {/* <a href="Markets" id="nodlt-sm">Markets</a> */}
          {/* <a href="userDetails" id="nodlt-sm">Dashboard</a> */}
          <a href="/" id="dlt-sm">
            About Us
          </a>
          <a href="/register/" id="dlt-sm">
            Register
          </a>
          {/* <a href="ContactUs" id="dlt-sm">
            Contact Us
          </a> */}
          
          <button id="header-button">
            <a href="/signin/" > Hello, Sign-In </a> &rarr;
          </button>
        </nav>
      </div>
    </header>
  );
}
