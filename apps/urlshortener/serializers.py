from rest_framework.serializers import ModelSerializer
from .models import Link


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('shortened_link', 'times_followed')
