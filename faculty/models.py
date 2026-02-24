from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department= models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField(blank=True)
    image = models.ImageField(upload_to='teachers/', default='teachers/default.png')
    joined_date=models.DateField(auto_now_add=True)

    def __clstr__(self):
        return self.name
