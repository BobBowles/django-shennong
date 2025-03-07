"""shennongAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView


# set the admin site header text
admin.site.site_header = '神农本草　Shen Nong Recipes And Herbs'
admin.site.site_title = '神农本草　Shen Nong'
admin.site.index_title = '神农本草　Shen Nong Site Administration'


urlpatterns = [
    path('', TemplateView.as_view(template_name="shennong/home.html"),
        name='home'),
    path('shennong/', include('shennong.urls')),
    path('admin/', admin.site.urls),
]
