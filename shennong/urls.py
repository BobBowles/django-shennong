from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.recipe_header, name="header"),
    url(r'^(?P<id>[0-9]+)/full/$', views.recipe_full, name="full"),
    url(r'^(?P<id>[0-9]+)/herb/$', views.herb, name="herb"),
]
