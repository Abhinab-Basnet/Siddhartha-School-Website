from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200, default="School Campus")
    description = models.TextField()
    is_holiday = models.BooleanField(default=False) # To highlight holidays in red

    def __str__(self):
        return f"{self.title} - {self.event_date}"