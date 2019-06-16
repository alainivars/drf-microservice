"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from drf-microservice import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.views import defaults
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.documentation import include_docs_urls
from my_api.rest.views import status_api, Icinga2API, FileAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication, Authorization, Users, Groups
    url(r'^api-auth/', include('rest_auth.urls')),
    url(r'^api-auth-token/$', rest_framework_views.obtain_auth_token,
        name='get_auth_token'),

    # Documentation
    url(r'^docs/', include_docs_urls(title='drf-microservice API')),

    # Probe live control
    path('icinga/', status_api, name='icinga'),
    path('icinga2/', Icinga2API.as_view(), name='icinga2'),

    # the API
    path('api/v1/file', FileAPI.as_view(), name='api_file'),

    # Some media files if you need it else remove it
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # To debug the error pages during development
    urlpatterns += [
        url(r'^400/$', defaults.bad_request),
        url(r'^403/$', defaults.permission_denied),
        url(r'^404/$', defaults.page_not_found),
        url(r'^500/$', defaults.server_error),
    ]
    # static/media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
