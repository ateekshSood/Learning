from django.shortcuts import render , HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request , "home.html")


def view_student(request):
    students = Student.objects.all()
    return render(request , 'studentshow.html' , {"students" : students})