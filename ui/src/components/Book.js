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
      <div>
        <div>{title}</div>
      </div>
    );
  }
}
