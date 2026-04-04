from django.urls import path
from . import views 

urlpatterns = [
    path("/home" , views.home , name="home"),
    path("/student", views.view_student, name="studentshow"),
] 