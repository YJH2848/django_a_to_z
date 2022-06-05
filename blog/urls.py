from django.urls import path
from . import views

urlpatterns = [
    #만약 /blog/뒤에 int형태의 값이 붙으면 blog/views.py의 single_post_page() 함수에 정의된 대로 처리하라
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]