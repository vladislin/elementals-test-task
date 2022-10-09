from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('original_link', 'shortened_link', 'times_followed', 'created')
    list_filter = ('times_followed', 'created')
    ordering = ('created',)
    filter_horizontal = ()


admin.site.register(Link, LinkAdmin)
