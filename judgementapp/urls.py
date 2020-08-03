from django.conf.urls import url, re_path
from django.views.generic import TemplateView

from judgementapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query$', views.query_list, name='query_list'),
    url(r'^query/qrels$', views.qrels, name='query_list'),
    url(r'^query/(?P<qId>\d+)/$', views.query, name='query'),
    url(r'^query/(?P<qId>\d+)/doc/(?P<docId>[A-Za-z0-9_\-\+\.]+)/$', views.document, name='document'),
    url(r'^query/(?P<qId>\d+)/doc/(?P<docId>[+A-Za-z0-9_\-\+\.]+)/judge/$', views.judge, name='judge'),
    re_path(r'^about/$', TemplateView.as_view(template_name='judgementapp/about.html')),
    re_path(r'^upload/$', TemplateView.as_view(template_name='judgementapp/upload.html')),
    url(r'^upload/save$', views.upload, name='upload')
]