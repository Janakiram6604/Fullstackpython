from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.hello_world, name='hello_world'),
    path('class/', views.helloindia.as_view(), name='helloindia'),
]