/* @flow */

import * as React from "react";
import { type Book } from "../types";

type Props = {
  book: Book
};

export default class BookCard extends React.Component<Props> {
  render() {
    const { title, isbn, available, branches } = this.props.book;

    return (
      <div className="book-container">
        <div className="book-title"><h2>{title}</h2></div>
        <ul>{branches.map(b => <li>{b}</li>)}</ul>
      </div>
    );
  }
}
