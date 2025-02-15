from django.contrib import admin
from django.urls import include, path
from .import views 

urlpatterns = [
    path('', views.products, name='products'),
    path('edit-course/', views.edit_course, name='edit-course'),
    path('courses/', views.courses, name='courses'), 
    path('course-new/', views.CourseNew, name='course-new'),
]