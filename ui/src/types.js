/* @flow */

export type Branch = string;

export type Book = {
  title: string,
  isbn: string,
  available: boolean,
  branches: $ReadOnlyArray<Branch>,
};

export type Results = Array<Book>;
