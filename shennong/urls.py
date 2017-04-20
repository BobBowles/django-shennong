from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.recipe_header, name='recipe_header'),
    url(r'^(?P<id>[0-9]+)/full/$', views.recipe_full, name='recipe_full'),
    url(r'^(?P<id>[0-9]+)/herb_header/$', views.herb_header, name='herb_header'),
]
