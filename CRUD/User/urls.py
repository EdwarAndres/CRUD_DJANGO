from django.urls import path
from User import views

urlpatterns = [
    path('login/', views.login),
    path('singup/', views.signup, name='signup'),
]