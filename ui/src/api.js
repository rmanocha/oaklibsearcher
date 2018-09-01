/* @flow */

import { API_URI } from "./config";
import type { Response } from "./types";

export function fetchBooks(): Promise<Response> {
  return fetch(`${API_URI}/available_books`)
    .then(resp => resp.json())
    .then(results => ({ tag: "success", results }))
    .catch(error => ({
      tag: "error",
      error
    }));
}
