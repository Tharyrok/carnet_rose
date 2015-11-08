from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from .models import Movement, ImportReport

from . import views


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Movement, template_name="accounts/home.haml"), name='accounts_home'),
    url(r'^import_report/(?P<pk>\d+)/$', DetailView.as_view(model=ImportReport, template_name="accounts/importreport_detail.haml"), name='accounts_importreport_detail'),
    url(r'^upload_record_bank_csv/$', views.UploadRecordBankCsv.as_view(), name='accounts_upload_record_bank_csv'),
)
