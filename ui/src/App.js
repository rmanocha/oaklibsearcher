/* @flow */

import * as React from "react";
import type { Response } from "./types";

import BookList from "./components/BookList";
import Loader from "./components/Loader";

import { withData, type Data } from "./withData";

class App extends React.Component<{ data: Data }> {
  _renderInner() {
    const { data } = this.props;
    switch (data.tag) {
      case "success": {
        const { results } = data;

        return <BookList books={results} />;
      }
      case "loading":
        return <Loader />;
      case "error":
        return <div>Error fetching</div>;
      default:
        return null;
    }
  }
  render() {
    return (
      <React.Fragment>
        <h1 className="header">OakLib Searcher</h1>
        {this._renderInner()}
      </React.Fragment>
    );
  }
}

export default withData(App);
