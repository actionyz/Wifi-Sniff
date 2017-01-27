"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from yz import views as yz_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',yz_views.index),
    url(r'^login.html$',yz_views.login),
    url(r'^index.html',yz_views.index),
    url(r'^test.html$',yz_views.test),
    url(r'^show_url.html$',yz_views.show_url),
    url(r'^image.html$',yz_views.image),
]
