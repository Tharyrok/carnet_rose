from django.conf.urls import patterns, url
from django.views.generic import ListView

from .models import Movement

from . import views


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Movement, template_name="accounts/home.haml"), name='accounts_home'),
    url(r'^upload_record_bank_csv/$', views.upload_record_bank_csv, name='accounts_upload_record_bank_csv'),
)
