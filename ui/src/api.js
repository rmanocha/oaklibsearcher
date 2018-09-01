/* @flow */

import { API_URI } from "./config";
import type { Results } from "./types";

type Response =
  | { tag: "success", results: Results }
  | { tag: "error", error: any };

export function fetchBooks(): Promise<Response> {
  return fetch(API_URI)
    .then(resp => resp.json())
    .then(results => ({ tag: "success", results }))
    .catch(error => ({
      tag: "error",
      error
    }));
}
