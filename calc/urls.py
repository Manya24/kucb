from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('',views.home, name=''),
    path('add/',views.add,name='add'),
    path("login",views.login,name="login"),
    path("register",views.register, name="register"),

]