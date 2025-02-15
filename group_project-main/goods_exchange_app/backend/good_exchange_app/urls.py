from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('authentication.urls')),
    path('', include('products.urls')),  # Sửa từ 'home.url' thành 'home.urls'
    path('admin/', admin.site.urls),
]
