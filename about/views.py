from django.shortcuts import render, get_object_or_404,redirect
from .models import HistoryEntry
from .models import AchievementCategory
from .forms import EntranceApplicationForm
# Create your views here.
def introduction(request):
    return render(request, 'about/introduction.html') 


def mission(request):
    return render(request, 'about/mission.html')


def prayer(request):
    return render(request, 'about/prayer.html')


def motto(request):
    return render(request, 'about/motto.html')

def logo(request):
    return render(request, 'about/logo.html')

def achievement_categories(request):
    categories = AchievementCategory.objects.all().order_by('-date_created')
    return render(request, 'about/achievement_list.html', {'categories': categories})

def achievement_detail(request, category_id):
    category = get_object_or_404(AchievementCategory, id=category_id)
    # Fetch the items using the related_name='items' we set in models.py
    items = category.items.all() 
    
    return render(request, 'about/achievement_detail.html', {
        'category': category, 
        'items': items  # Pass the items to the template!
    })


def history(request):
    history_entries = HistoryEntry.objects.all().order_by('year_or_era')
    return render(request, 'about/history.html', {'history_entries': history_entries})



def admission_form(request):
    if request.method == 'POST':
        form = EntranceApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'about/success.html', {'message': 'Application submitted successfully!'})
    else:
        form = EntranceApplicationForm()
    return render(request, 'about/admission.html', {'form': form})