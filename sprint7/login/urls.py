from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('signout/', views.signout, name='signout')
]
