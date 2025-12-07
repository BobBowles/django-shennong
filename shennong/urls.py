from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<id>[0-9]+)/recipe_header/$',
        views.recipe_header,
        name='recipe_header'
    ),
    re_path(r'^(?P<id>[0-9]+)/recipe_full_1col/$',
        views.recipe_full_1col,
        name='recipe_full_1col'
    ),
    re_path(r'^(?P<id>[0-9]+)/recipe_full_2col/$',
        views.recipe_full_2col,
        name='recipe_full_2col'
    ),
    re_path(r'^herb/$', views.herb_index, name='herb_index'),
    re_path(r'^(?P<id>[0-9]+)/herb_header/$',
        views.herb_header, name='herb_header'
    ),
    re_path(r'^(?P<id>[0-9]+)/herb_full/$',
        views.herb_full,
        name='herb_full'
    ),
]
