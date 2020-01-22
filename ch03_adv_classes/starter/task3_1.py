import colorama
import jinja2
import jinja2.exceptions
import requests

# don't forget to import your movie.py module here!

key = '23cf8b21d9a3bfd615076491d6bae442'
search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'


def render_movie(movie):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./tmpl'))
    try:
        tmpl = env.get_template('movie.jinja')
        # render movie results here.  Place a line calling render() of the tmpl object
        # and then passing in a movie object as a keyword

    except (jinja2.exceptions.TemplateNotFound, jinja2.exceptions.TemplateError) as err:
        results = f'Error rendering movie: {err}'

    return results


# Step 4. Prompt the user for a movie phrase to search for, retrieve a list of search results
#         as JSON (use the search_url above).  Use the requests module to help you to make the request.
#
#         The key is provided above and must be inserted (along with the movie phrase) into the search_url.
#         Use the slide (2 of 3) in the materials to understand the structure of the returned data.  Extract
#         a list of the titles.
#         Display the list and allow the user to select one from the list.
#
#         Remember that data returned is in JSON format and must be parsed.


# Step 5. Prompt the user to select a specific title.  Use this selection to
#         look back into the search results and extract the id field from the desired
#         movie.  Again, refer to the slide in the student manual (2 of 3) on how to obtain the id and
#         how to insert it into the details_url.
#
#         This id must be inserted into the details_url above to allow for
#         making a second (more detailed) request.  Perform a detailed
#         search (use the details_url above) inserting the key in the url again also.
#
#         Remember: the detailed data is also returned in JSON format.


# Step 6. Get the returned results and create a Movie instance from the returned
#         data.


# Step 7. Using the movie object created in step 6, render the movie data using the
#         provided Jinja2 templates.  This can be done by completing the render_movie() method above
#         and then passing the new movie instance into it.
#
#         In the render_movie() method, the following will invoke the template:
#               results = tmpl.render(movie=movie)

