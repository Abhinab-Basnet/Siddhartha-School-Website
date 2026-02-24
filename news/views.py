from django.shortcuts import render
from django.shortcuts import render
from .models import Notices

# Add this function
def notice_list(request):
    notices = Notices.objects.all()
    return render(request, 'news/notice_list.html', {'notices': notices})