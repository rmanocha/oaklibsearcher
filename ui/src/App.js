/* @flow */

import * as React from "react";
import type { Response } from "./types";

import Book from "./components/Book";
import Loader from "./components/Loader";

import { withData, type Data } from "./withData";

class App extends React.Component<{ data: Data }> {
  render() {
    const { data } = this.props;
    switch (data.tag) {
      case "success": {
        const { results } = data;

        return results.map(r => <Book book={r} />);
      }
      case "loading":
        return <Loader />;
      case "error":
      default:
        return null;
    }
  }
}

export default withData(App);
