/* @flow */

import * as React from "react";
import type { Response } from "./types";

import { fetchBooks } from "./api";

export type Data = Response | { tag: 'loading' };


export function withData<P: Object>(
  C: React.ComponentType<P & { data: Data }>
): React.ComponentType<P> {
  type State = {
    data: Data
  };

  class WithData extends React.Component<P, State> {
    state = {
      data: { tag: 'loading' },
    };

    componentDidMount() {
      this._fetchData();
    }

    _fetchData() {
      fetchBooks().then(resp => {
        this.setState({ data: resp });
      });
    }

    render() {
      const { data } = this.state;
      if (data) {
        const props = {
          ...this.props,
          data
        };

        return <C {...props} />;
      } else {
        return null;
      }
    }
  }

  return WithData;
}
