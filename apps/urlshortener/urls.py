from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShortenerViewSet

app_name = 'urlshortener'

router = DefaultRouter()
router.register('', ShortenerViewSet, 'shortener')

urlpatterns = [
    path('', include(router.urls))
]
