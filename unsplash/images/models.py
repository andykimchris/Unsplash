from django.db import models


class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

    class Meta:
        ordering = ['place']

    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def search_by_category(cls, search_category):
        category = cls.objects.filter(category__icontains=search_category)
        return category
