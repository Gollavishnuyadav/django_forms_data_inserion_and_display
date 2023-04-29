from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Url=models.URLField()
    # Gender=models.CharField(max_length=100)
    # Password=models.CharField(max_length=100)
    # Address=models.CharField(max_length=100)
    # Course=models.CharField(max_length=100)
    # Radio=models.CharField(max_length=100)

    def __str__(self):
        return self.Name