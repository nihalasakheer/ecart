from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('my_account/', views.my_account, name='my_account'),
]