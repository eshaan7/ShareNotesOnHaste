from django.db import models

# Create your models here.
class Notes(models.Model):
    note = models.TextField()
    
    def __str__(self):
        return f"{self.note}"