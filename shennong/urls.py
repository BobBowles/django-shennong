from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/recipe_header/$',
        views.recipe_header,
        name='recipe_header'
    ),
    url(r'^(?P<id>[0-9]+)/recipe_full/$',
        views.recipe_full,
        name='recipe_full'
    ),
    url(r'^herb/$', views.herb_index, name='herb_index'),
    url(r'^(?P<id>[0-9]+)/herb_header/$',
        views.herb_header, name='herb_header'
    ),
    url(r'^(?P<id>[0-9]+)/herb_full/$',
        views.herb_full,
        name='herb_full'
    ),
]
