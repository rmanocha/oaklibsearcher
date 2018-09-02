/* @flow */

import { API_URI } from "./config";
import type { Response } from "./types";

export function fetchBooks(): Promise<Response> {

  // return Promise.resolve({ tag: 'success', results: data });

  return fetch(`${API_URI}/available_books`)
    .then(resp => resp.text())
    .then(results => ({ tag: "success", results: JSON.parse(results) }))
    .catch(error => ({
      tag: "error",
      error
    }));
}

const data = [
  {
    "available": true, 
    "branches": [
      "Asian Library Classics", 
      "Main Library Storage - Ask at Desk", 
      "Montclair Library", 
      "Temescal Library"
    ], 
    "isbn": "9780684833392", 
    "title": "Catch-22"
  }, 
  {
    "available": true, 
    "branches": [
      "Eastmont Library", 
      "Golden Gate Library", 
      "Lakeview Library", 
      "Main Library", 
      "Main Library", 
      "Piedmont Library", 
      "Rockridge Library"
    ], 
    "isbn": "9780670022953", 
    "title": "The better angels of our nature : why violence has declined"
  }, 
  {
    "available": true, 
    "branches": [
      "81st Avenue Library", 
      "Lakeview Library Hot Picks", 
      "Main Library"
    ], 
    "isbn": "9781594204876", 
    "title": "Grant"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780553447439", 
    "title": "Evicted : poverty and profit in the American city"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780143115267", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "Asian Library", 
      "Brookfield Library", 
      "Chavez Library", 
      "Eastmont Library", 
      "Elmhurst Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Melrose Library", 
      "Montclair Library", 
      "Rockridge Library", 
      "Rockridge Library", 
      "Rockridge Library"
    ], 
    "isbn": "9780802123459", 
    "title": "The sympathizer : a novel"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780141186351", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "Main Library", 
      "Main Library", 
      "Piedmont Library", 
      "Rockridge Library"
    ], 
    "isbn": "9780525427575", 
    "title": "Enlightenment now : the case for reason, science, humanism, and progress"
  }, 
  {
    "available": true, 
    "branches": [
      "Temescal Library"
    ], 
    "isbn": "9781101886724", 
    "title": "Waking gods"
  }, 
  {
    "available": true, 
    "branches": [
      "81st Avenue Library"
    ], 
    "isbn": "9780316547611", 
    "title": "The power : a novel"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780812536355", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "Asian Library Adult Paperback Browsing", 
      "Asian Library Adult Paperback Browsing", 
      "Main Library"
    ], 
    "isbn": "9780765316974", 
    "title": "The last colony"
  }, 
  {
    "available": true, 
    "branches": [
      "Asian Library Adult Paperback Browsing", 
      "Asian Library Adult Paperback Browsing", 
      "Lakeview Library", 
      "Main Library", 
      "Melrose Library", 
      "Montclair Library"
    ], 
    "isbn": "9780765316981", 
    "title": "Zoe's tale"
  }, 
  {
    "available": true, 
    "branches": [
      "Dimond Library", 
      "Main Library", 
      "Rockridge Library", 
      "Temescal Library"
    ], 
    "isbn": "9780765333513", 
    "title": "The human division"
  }, 
  {
    "available": true, 
    "branches": [
      "Chavez Library - Young Adult", 
      "Dimond Library - Young Adult", 
      "Dimond Library Hot Picks", 
      "Eastmont Library", 
      "Eastmont Library", 
      "M.L. King Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Main Library", 
      "Temescal Library"
    ], 
    "isbn": "9781501126062", 
    "title": "Sing, unburied, sing : a novel"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780786226740", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780552135399", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "81st Avenue Library", 
      "81st Avenue Library", 
      "African American Museum and Library", 
      "Brookfield Library", 
      "Elmhurst Library", 
      "Golden Gate Library", 
      "Main Library", 
      "Piedmont Library Hot Picks", 
      "Rockridge Library", 
      "Temescal Library", 
      "West Oakland LibraryAfrican AmericanCollection"
    ], 
    "isbn": "9780399590566", 
    "title": "We were eight years in power : an American tragedy"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780060593087", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780060733353", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780060750862", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "81st Avenue Library", 
      "Chavez Library", 
      "Dimond Library", 
      "Elmhurst Library", 
      "Lakeview Library", 
      "Main Library", 
      "Main Library", 
      "Montclair Library", 
      "Piedmont Library", 
      "Rockridge Library", 
      "Temescal Library", 
      "West Oakland Library", 
      "West Oakland Library"
    ], 
    "isbn": "9781594204111", 
    "title": "The signal and the noise : why most predictions fail-- but some don't"
  }, 
  {
    "available": true, 
    "branches": [
      "Dimond Library"
    ], 
    "isbn": "9780205313426", 
    "title": "The elements of style"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780765388896", 
    "title": "The collapsing empire [electronic resource]"
  }, 
  {
    "available": true, 
    "branches": [
      "Main Library", 
      "Montclair Library", 
      "Rockridge Library"
    ], 
    "isbn": "9781416596585", 
    "title": "In the plex : how Google thinks, works, and shapes our lives"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780575097360", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "81st Avenue Library", 
      "Brookfield Library", 
      "Eastmont Library", 
      "Golden Gate Library", 
      "Main Library", 
      "Main Library", 
      "Rockridge Library", 
      "Temescal Library"
    ], 
    "isbn": "9780553448122", 
    "title": "Artemis : a novel"
  }, 
  {
    "available": true, 
    "branches": [
      "Main Library", 
      "Main Library", 
      "Melrose Library", 
      "Montclair Library", 
      "Rockridge Library", 
      "Temescal Library"
    ], 
    "isbn": "9780553380958", 
    "title": "Snow crash"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780465069903", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780060521998", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "Unable to retrieve branches"
    ], 
    "isbn": "9780375751516", 
    "title": "The picture of Dorian Gray"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780241309254", 
    "title": ""
  }, 
  {
    "available": true, 
    "branches": [
      "Chavez Library", 
      "Dimond Library", 
      "Main Library", 
      "Main Library Storage - Ask at Desk"
    ], 
    "isbn": "9780374227340", 
    "title": "The origins of political order : from prehuman times to the French Revolution"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9781508243243", 
    "title": "Principles [sound recording] : life & work"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780195374612", 
    "title": "A guide to the good life : the ancient art of Stoic joy"
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780553283686", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780340839935", 
    "title": ""
  }, 
  {
    "available": false, 
    "branches": [], 
    "isbn": "9780099578512", 
    "title": ""
  }
];
