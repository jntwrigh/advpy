from django.conf.urls import url

from racerapp import views

urlpatterns = [
    url(r'^$', views.list_races, name='racerapp_list_races'),
    url(r'register/(?P<racename>[^/]+)', views.register, name='racerapp_register'),
    url(r'submit/', views.submit, name='racerapp_submit_reg'),
    url(r'participants/(?P<racename>[^/]+)', views.participants, name='racerapp_get_participants'),

]
