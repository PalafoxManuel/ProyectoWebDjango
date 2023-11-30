from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('foxshop/', include("TiendaBien.urls")),
    path('admin/', admin.site.urls)
]
