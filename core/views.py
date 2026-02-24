from django.shortcuts import render,redirect
from news.models import Notices
from django.contrib import messages
from .models import ContactMessage

# Create your views here.
def home(request):
    all_notices= Notices.objects.all().order_by('-date_posted')
    context = {
        'notices': all_notices
    }
    return render(request, 'core/index.html',context)

def contact(request):
    if request.method == "POST":
        # Later we will add logic to save messages to the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
        
    return render(request, 'core/contact.html')