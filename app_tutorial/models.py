from django.db import models

# Create your models here.
class Subjects(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    

class Topics(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.section
    
class Entries(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    section = models.ForeignKey(Topics, on_delete=models.CASCADE)
    info = models.TextField()
    code = models.TextField(blank=True)
    links = models.TextField(blank=True)

    def __str__(self):
        return self.info