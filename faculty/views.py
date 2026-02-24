from django.shortcuts import render
from .models import Teacher

# Create your views here.
def faculty_list(request):
    teachers=Teacher.objects.all()
    return render(request, 'faculty/faculty_list.html',{'teachers':teachers})
