from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(?P<id>\d+)/$', views.show_image_id, name="image"),
    url(r'^image/(?P<id>\d+)/delete/$', views.delete_image, name="delete_image"),
    url(r'^search/', views.search, name='search')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
