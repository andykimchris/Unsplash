from django.db import models


class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

    class Meta:
        ordering = ['place']

    def save_location(self):
        self.save()
