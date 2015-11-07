from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from members.views import ffdn_api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="admin", permanent=False)),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^isp.json$', ffdn_api),
    url(r'^admin/', include(admin.site.urls)),
)
