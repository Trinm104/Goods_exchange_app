from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('list1/', views.list1, name='list1'),
    path('list1/see/', views.see, name='see'),  # Nested URL pattern
    path('list2/', views.list2, name='list2'),
    path('dstd/', views.dstd, name='dstd'),
    path('list3/', views.list3, name='list3'),
    path('see/', views.see, name='see'),
    path('list4/', views.list4, name='list4'),
]
