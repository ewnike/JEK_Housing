from django.urls import path, re_path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "housing"

urlpatterns = [
    path( '', homepage , name = "index"),
    path('property_list', PropertyListView.as_view(), name = 'property_list'),
    path('about_us', about_us, name = 'about_us'),
    path('invest', invest, name = 'invest')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
