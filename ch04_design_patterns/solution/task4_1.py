"""
    task7_1.py      -       This implementation is the same as the task3_1
                            implemenation except that it moves some of the
                            app functions into app.py and provides unit tests.

"""
import colorama

from ch04_design_patterns.solution.app import movie_search, detailed_search, render_movie

key = '23cf8b21d9a3bfd615076491d6bae442'
search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'


search_term = input('Enter a movie phrase: ')
search_dict = movie_search(search_url, key, search_term)

movie_list = search_dict.get('results', [])
for idx, movie in enumerate(movie_list, 1):
    print(colorama.Fore.RED, '{0} - {1}'.format(idx, movie.get('title', '(no title)')))

selected = input('Enter number for details: ')
id = movie_list[int(selected) - 1].get('id')
if id:
    m = detailed_search(details_url, key, id)
    print(colorama.Fore.GREEN, render_movie(m))
