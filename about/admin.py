from django.contrib import admin
from .models import HistoryEntry
from .models import AchievementCategory, AchievementItem

from .models import EntranceApplication

@admin.register(HistoryEntry)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('year_or_era', 'title')


class AchievementItemInline(admin.TabularInline):
    model = AchievementItem
    extra = 3 # Matches your gallery's 3 empty slots

@admin.register(AchievementCategory)
class AchievementCategoryAdmin(admin.ModelAdmin):
    inlines = [AchievementItemInline]
    list_display = ('title', 'date_created')




@admin.register(EntranceApplication)
class EntranceApplicationAdmin(admin.ModelAdmin):
    # This makes it easy to see key info at a glance in the list view
    list_display = ('student_name_en', 'grade_applying_for', 'phone_number', 'submitted_at')
    # Allows searching by name or grade
    search_fields = ('student_name_en', 'grade_applying_for')
    # Adds a filter on the right sidebar
    list_filter = ('grade_applying_for', 'submitted_at')
    # Prevents accidental deletion of application records
    readonly_fields = ('submitted_at',)