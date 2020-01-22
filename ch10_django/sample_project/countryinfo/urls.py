from django.conf.urls import url
from countryinfo import views

urlpatterns = [
    url(r'^(?P<country>[a-zA-Z]+)/(?P<region>[a-zA-Z]+)', views.get_info, name='get_country_info'),
    url(r'^$', views.index2, name='default_call'),
    #url(r'^$', views.index, name='countryinfo_index'),
]
