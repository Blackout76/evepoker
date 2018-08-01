from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<tableID>\d+)/$', views.joinTable),
    url(r'^$', views.tables),
    url(r'^newtable', views.newtable),
    url(r'^leavetable/$', views.leaveTable),
]
