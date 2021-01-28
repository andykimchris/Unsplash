from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('image/(?P<id>\d+)/$', views.show_image_id, name="image"),
    re_path('image/(?P<id>\d+)/delete/$', views.delete_image, name="delete_image"),
    path('search_results/', views.search_results, name='search_results'),
    path('search_location/', views.search_location, name='search_location')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
