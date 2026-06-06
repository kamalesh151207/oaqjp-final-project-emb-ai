from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam, name='home'),
    path('exam/', views.exam, name='exam'),
    path('submit/', views.submit, name='submit'),
    path('show_exam_result/', views.show_exam_result, name='show_exam_result'),
]