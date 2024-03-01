from django.db import models

# Create your models here.
class subjects(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    
class entry(models.Model):
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    info = models.TextField()
    code = models.TextField(blank=True)
    links = models.TextField(blank=True)