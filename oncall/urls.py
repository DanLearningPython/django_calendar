from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.event_create, name='event_create'),
    url(r'^update/(\d+)/$', views.event_update, name='event_update'),
    url(r'^event_feed/$', views.event_feed, name='test'),
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', auth_views.login, {'template_name': 'oncall/login.html', 'redirect_field_name' : 'index'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout', ),
]