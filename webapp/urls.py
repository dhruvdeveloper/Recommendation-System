from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^pqrst$', views.index3, name='index3'),
    url(r'^bookjson$', views.index4, name='index4'),
    url(r'^index/signup', views.authentication, name='authentication'),
    url(r'^index/login', views.login, name='login'),
    url(r'^index/show', views.show, name='show'),
    url(r'^index/music', views.music, name='music'),
    url(r'^index/book', views.book, name='book'),
    url(r'^index/logout', views.logout, name='logout'),
    url(r'^admin/backend', views.admin, name='admin'),
    #url(r'^x', views.my, name='my')
]
