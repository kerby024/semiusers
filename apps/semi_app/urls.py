from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.display),
    url(r'^adduser$', views.add),
    url(r'^register$', views.register),
    url(r'^user/(?P<userid>\d+)$', views.users),
    url(r'^user/(?P<userid>\d+)/edit$', views.edit),
    url(r'^update$', views.update),
    url(r'^user/(?P<userid>\d+)/delete$', views.delete),
    ]