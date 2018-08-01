from django.contrib import admin
from django.conf.urls import url, include
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^help/', views.help, name='help'),
    url(r'^users/', include('users.urls')),
    url(r'^tables/', include('tables.urls')),
    url(r'^admin/', admin.site.urls),
]
