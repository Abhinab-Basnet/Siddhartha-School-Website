from django.shortcuts import render,redirect
from django.utils import timezone
from news.models import Notices
from django.contrib import messages
from events.models import Event
from gallery.models import Photo
from .models import ContactMessage

# Create your views here.
def home(request):
    context = {
        # Notices
        'notices': Notices.objects.order_by('-date_posted')[:5],
        'latest_notices': Notices.objects.order_by('-date_posted')[:10],
        
        # Events
        'upcoming_events': Event.objects.filter(
            event_date__gte=timezone.now().date()
        ).order_by('event_date')[:4],
        
        # Gallery
        'gallery_photos': Photo.objects.order_by('-id')[:5],
        
        # # School Info (Using the model we created in the 'about' app)
        # 'school_info': SchoolCoreInfo.objects.first(),
    }
    return render(request, 'core/index.html', context)

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