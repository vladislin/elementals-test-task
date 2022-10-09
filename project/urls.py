from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.urlshortener.views import Redirector

schema_view = get_schema_view(
    openapi.Info(
        title="Coi Test Task API",
        default_version='v1',
        description="Test description",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.users.urls')),
    path('shortener/', include('apps.urlshortener.urls')),
    path('<str:shortener_link>/', Redirector.as_view(), name='redirector'),
]
