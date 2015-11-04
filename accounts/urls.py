from django.conf.urls import patterns, url
from django.views.generic import ListView

from .models import Movement


urlpatterns = patterns('accounts.views',
    url(r'^$', ListView.as_view(model=Movement, template_name="accounts/home.haml"), name='accounts_home'),
)
