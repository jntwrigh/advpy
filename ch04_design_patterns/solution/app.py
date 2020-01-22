"""

        app.py                  Is a refactored module from the task3_1 solution
                                in which each function previously in the task3_1.py
                                driver file was moved into this file.

"""
import sys

import jinja2
import jinja2.exceptions
import requests

import ch04_design_patterns.solution.movie.movie as movie_mod


def movie_search(search_url: str, key: str, search_term: str):
    try:
        results = requests.get(search_url.format(key=key, title=search_term)).json()
    except requests.RequestException as re:
        print(f'Requests Error: {re}')
        sys.exit(42)

    return results


def detailed_search(details_url: str, key: str, movie_id: str) -> movie_mod.Movie:
    try:
        results = requests.get(details_url.format(key=key, id=movie_id)).json()
        m = movie_mod.Movie(**results)
    except requests.RequestException as re:
        print(f'Error: {re}')
        sys.exit(42)

    return m


def render_movie(movie, tmpl_path='./tmpl'):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(tmpl_path))
    try:
        tmpl = env.get_template('movie.jinja')
        results = tmpl.render(movie=movie)
    except (jinja2.exceptions.TemplateNotFound, jinja2.exceptions.TemplateError) as err:
        results = f'Error rendering movie: {err}'
    return results
