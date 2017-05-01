from django.conf.urls import url

from . import views

app_name = 'ucp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^(?P<pk>[0-9]+)/$', views.ReportsView.as_view(), name='reports'),
]