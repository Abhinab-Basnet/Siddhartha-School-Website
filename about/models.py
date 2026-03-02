from django.db import models

class HistoryEntry(models.Model):
    year_or_era = models.CharField(max_length=100, help_text="e.g., '1988' or 'The Early Years'")
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "History Entries"
        ordering = ['year_or_era'] # Keeps history chronological

    def __str__(self):
        return f"{self.year_or_era} - {self.title}"
    


class AchievementCategory(models.Model):
    title = models.CharField(max_length=200) # e.g., "Academic Excellence 2082"
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='achievement_covers/')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Achievement Categories"

    def __str__(self):
        return self.title

class AchievementItem(models.Model):
    category = models.ForeignKey(AchievementCategory, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='achievements/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Achievement: {self.title}"