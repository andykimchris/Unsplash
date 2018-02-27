from django.test import TestCase
from .models import Category, Gallery, Location


class CategoryTestClass(TestCase):

    def setUp(self):
        self.food = Category(name='Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    def test_save_method(self):
        self.andy.save_category()
        category_name = Category.objects.all()
        self.assertTrue(len(category_name) > 0)


class LocationTestClass(TestCase):

    def setUp(self):
        self.nairobi = Location(place='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Location))

    def test_save_method(self):
        self.andy.save_location()
        location_name = Location.objects.all()
        self.assertTrue(len(location_name) > 0)


class GalleryTestClass(TestCase):

    def setUp(self):
        self.image = Gallery(id='6', image='/gallery/fabian-irsara-92113-unsplash.jpg', width_field='5046', height_field='3364', image_name='Hacking at Cafe Bistro',
                             description='Having coffee and clearing accounts in school, morning time has never felt so good', url='https://unsplashbyandy.herokuapp.com/media/gallery/fabian-irsara-92113-unsplash.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Gallery))

    def test_save_method(self):
        self.imsgr.save_images()
        image_name = Gallery.objects.all()
        self.assertTrue(len(image_name) > 0)

    def tearDown(self):
        Gallery.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
