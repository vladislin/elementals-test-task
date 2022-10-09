from django.conf import settings
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Link
from .permissions import IsOwnerOrAdmin
from .serializers import LinkSerializer


class ShortenerViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_admin:
            return Link.objects.all()
        else:
            return Link.objects.filter(owner=self.request.user)
    serializer_class = LinkSerializer
    permission_classes = [IsOwnerOrAdmin]


class Redirector(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL + '/' + self.kwargs['shortener_link']
        obj = Link.objects.get(shortened_link=shortener_link)
        obj.increase_short_link_counter()
        return redirect(obj.original_link)
