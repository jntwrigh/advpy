from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

import racerapp.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^races/', include(racerapp.urls)),
    url(r'^$', RedirectView.as_view(pattern_name='racerapp_list_races', permanent=False))
]
