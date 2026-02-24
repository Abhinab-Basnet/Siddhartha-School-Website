from django.db import models

# Create your models here.
class Notices(models.Model):
    CATEGORY_CHOICES=[
        ('General', 'General'),
        ('Exam', 'Examination'),
        ('Holiday', 'Holiday'),
        ('Event', 'Event'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='General')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']