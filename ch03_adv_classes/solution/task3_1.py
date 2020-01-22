import colorama
import jinja2
import jinja2.exceptions
import requests

import ch03_adv_classes.solution.movie.movie as movie_mod

key = '23cf8b21d9a3bfd615076491d6bae442'
search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'


def render_movie(movie):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./tmpl'))
    try:
        tmpl = env.get_template('movie.jinja')
        results = tmpl.render(movie=movie)
    except (jinja2.exceptions.TemplateNotFound, jinja2.exceptions.TemplateError) as err:
        results = f'Error rendering movie: {err}'
    return results


search_term = input('Enter a movie phrase: ')
search_dict = {}
try:
    search_dict = requests.get(search_url.format(key=key, title=search_term)).json()
except requests.RequestException as re:
    pass

movie_list = search_dict.get('results', [])
for idx, movie in enumerate(movie_list, 1):
    print(colorama.Fore.RED, f'{idx} - {movie.get("title", "(no title)")}')

selected = input('Enter number for details: ')
id = movie_list[int(selected) - 1].get('id')
if id:
    details = requests.get(details_url.format(key=key, id=id)).json()
    m = movie_mod.Movie(**details)
    print(colorama.Fore.GREEN, render_movie(m))
