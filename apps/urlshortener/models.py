from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings


class Link(models.Model):
    original_link = models.URLField()
    shortened_link = models.URLField(unique=True, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    times_followed = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def increase_short_link_counter(self):
        self.times_followed += 1
        self.save()

    @classmethod
    def shortener(cls):
        while True:
            random_string = ''.join(choices(ascii_letters, k=6))
            new_link = settings.HOST_URL + '/' + random_string

            if not cls.objects.filter(shortened_link=new_link).exists():
                break

        return new_link

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            new_link = self.shortener()
            self.shortened_link = new_link
        return super().save(*args, **kwargs)


