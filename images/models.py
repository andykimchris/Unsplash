from django.db import models
from django.urls import reverse


class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

    class Meta:
        ordering = ['place']

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    image_name = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    url = models.URLField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['-image']

    @classmethod
    def my_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        value = cls.objects.filter(
            category__name__icontains=search_term)
        return value

    @classmethod
    def search_by_location(cls, search_term):
        value = cls.objects.filter(
            location__place__icontains=search_term)
        return value

    def save_images(self):
        self.save()

    def get_delete_url(self):
        return reverse("gallery:delete_image", kwargs={"id": self.id})

    def get_absolute_url(self):
        return reverse('gallery:image', kwargs={'id': self.id})

    def update_image(self, id):
        pass

    def filter_by_location(location):
        pass

    def search_image(category):
        pass
