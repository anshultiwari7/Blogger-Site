"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from userprofile import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^blogs',views.blog2List.as_view()),
    # url(r'^user',views.userList.as_view()),
    # url(r'^login',views.LoginList.as_view()),
    url(r'^login',views.login, name='login'),
    # url(r'^test',views.test),
    url(r'^signup',views.signup, name='signup'),
    url(r'^viewblog/(?P<id>[0-9]+)/$',views.view_blog),
    url(r'^logout',views.logout),
    url(r'^delete/(?P<id>[0-9]+)/$',views.delete),
    url(r'^edit/(?P<id>[0-9]+)/$',views.edit),
    url(r'^blog/(?P<id>[0-9]+)/$',views.blog),
    url(r'^mainpage',views.mainpage, name='mainpage'),
]
