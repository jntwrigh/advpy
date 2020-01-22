from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from countryinfo.models import Region


def index(request):
    return HttpResponse('Country Information')


def index2(request):
    """
        Revised version of index() above.  This one supports loading a template (discussed
        in student manual in the section on Ajax).
    """
    template = loader.get_template('info3.html')
    return HttpResponse(template.render())

# def get_info(request, country, region):
#     """
#         Version 1
#         Our first version of get_info() as discussed in the student manual, before the next version (shown below)
#         Using URL of: http://localhost:8000/info/USA/California should cause this function
#          to be invoked.
#     """
#     return HttpResponse(Region.objects.get(country=country, name=region))



# def get_info(request, country, region):
#     """
#         Version 2
#         This version of get_info() supports bad results in the URL (meaning, no object
#         was found in the database.  (e.g. http://localhost:8000/info/foo/bar returns no objects)
#     """
#     try:
#         r = Region.objects.get(country=country, name=region)
#         results = str(r)
#     except ObjectDoesNotExist:
#         results = 'Country / Region combination not found.'
#     return HttpResponse(results)


def get_info(request, country, region):
    """
        Version 3
        This version uses templating.  It is shown in the student manual after introducing templates.
    """
    r = Region(name='Not found.', country='None.', population='Unknown', abbreviation='NA')
    try:
        r = Region.objects.get(country=country, name=region)
    except ObjectDoesNotExist:
        pass
    # return render(request, 'info1.html', vars(r))
    # return render(request, 'info2.html', vars(r))

    # the code below (added for the Ajax discussion), converts the Region into JSON
    data = serializers.serialize('json', (r,))
    response = HttpResponse(data)
    response['content_type'] = 'application/json'
    return response
