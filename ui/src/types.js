/* @flow */

export type Branch = string;

export type Book = {
  title: string,
  isbn: string,
  available: boolean,
  branches: $ReadOnlyArray<Branch>,
};

export type Results = Array<Book>;

export type Response =
  | { tag: "success", results: Results }
  | { tag: "error", error: any };

