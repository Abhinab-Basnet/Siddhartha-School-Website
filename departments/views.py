from django.shortcuts import render, get_object_or_404
from .models import Department
from faculty.models import Teacher

# Create your views here.
def department_list(request):
    depts= Department.objects.all()
    return render(request,'departments/list.html',{'departments':depts})

def department_detail(request,slug):
    dept=get_object_or_404(Department,slug=slug)
    dept_teachers = Teacher.objects.filter(department=dept.name)
    context={
        'dept':dept,
        'teachers':dept_teachers,
    }
    return render(request ,'departments/detail.html',context)
