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
from rest_framework import permissions
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from my_api.rest.views import status_api, Icinga2API, FileAPI
if settings.DEBUG_URL:
    from my_api.rest.views import \
        api_handler400, api_handler403, api_handler404, api_handler500


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="DRF Microservice RESTFUL",
        terms_of_service="/terms/",
        contact=openapi.Contact(email="alain.ivars@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(
        r'^swagger/openapi(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json-or-yaml'
    ),
    url(
        r'^swagger/openapi/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-openapi-ui'
    ),
    url(
        r'^swagger/redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

urlpatterns += [
    path('admin/', admin.site.urls),

    # Authentication, Authorization, Users, Groups
    url(r'^api-auth/', include('rest_auth.urls')),
    url(
        r'^api-auth-token/$',
        rest_framework_views.obtain_auth_token,
        name='get_auth_token'
    ),

    # Documentation
    url(r'^docs/', include_docs_urls(title='drf-microservice API')),

    # Probe live control
    path('icinga/', status_api, name='icinga'),
    path('icinga2/', Icinga2API.as_view(), name='icinga2'),

    # the API
    path('api/v1/file', FileAPI.as_view(), name='api_file'),

    # Some media files if you need it else remove it
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG_URL:
    # To debug the error pages during development
    urlpatterns += [
        url(r'^400/$', api_handler400, name='handler400'),
        url(r'^403/$', api_handler403, name='handler403'),
        url(r'^404/$', api_handler404, name='handler404'),
        url(r'^500/$', api_handler500, name='handler500'),
    ]
    # static/media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'my_api.rest.views.api_handler400'
handler403 = 'my_api.rest.views.api_handler403'
handler404 = 'my_api.rest.views.api_handler404'
handler500 = 'my_api.rest.views.api_handler500'
