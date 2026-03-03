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


class EntranceApplication(models.Model):
    # Personal Info
    student_name_en = models.CharField(max_length=200)
    student_name_np = models.CharField(max_length=200, blank=True)
    dob_ad = models.DateField()
    dob_bs = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    
    # Parent/Guardian Details
    father_name = models.CharField(max_length=200)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=200)
    mother_occupation = models.CharField(max_length=100)
    
    # Contact Info
    permanent_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    
    # Academic/Misc
    last_school_attended = models.CharField(max_length=200)
    grade_applying_for = models.CharField(max_length=10)
    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name_en