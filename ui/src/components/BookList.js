/* @flow */

import * as React from "react";
import { type Book } from "../types";

import BookCard from "./Book";

type Props = {
  books: $ReadOnlyArray<Book>
};

export default class BookList extends React.Component<Props> {
  render() {
    const { books } = this.props;

    return (
      <div className="book-list">
        {books.map(b => <BookCard book={b} key={b.isbn} />)}
      </div>
    );
  }
}
