from django.contrib import admin
from .models import HistoryEntry
from .models import AchievementCategory, AchievementItem

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