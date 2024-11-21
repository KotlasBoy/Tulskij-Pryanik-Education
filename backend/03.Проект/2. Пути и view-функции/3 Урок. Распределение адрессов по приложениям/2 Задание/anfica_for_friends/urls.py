
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
]