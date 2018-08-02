from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^oauth$', views.oauth, name='oauth'),
]
