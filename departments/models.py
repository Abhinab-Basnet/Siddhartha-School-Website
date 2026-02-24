from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    hod_name=models.CharField(max_length=100, verbose_name="Head of Department")
    contact_email=models.EmailField()
    cover_image = models.ImageField(upload_to='departments/')

    def __str__(self):
        return self.name
    
    
