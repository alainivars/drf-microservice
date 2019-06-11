"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from {{cookiecutter.github_repository_name}} import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.documentation import include_docs_urls
from {{cookiecutter.app_name}}.rest import views_users
from {{cookiecutter.app_name}}.rest.views import status_api, Icinga2API, FileAPI

router = routers.DefaultRouter()
router.register(r'users', views_users.UserViewSet)
router.register(r'groups', views_users.GroupViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token,
        name='get_auth_token'),
    path('icinga/', status_api, name='icinga'),
    path('icinga2/', Icinga2API.as_view(), name='icinga2'),
    path('project/api/v1/file', FileAPI.as_view(), name='api_file'),
]
