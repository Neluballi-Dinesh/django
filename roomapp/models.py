from django.db import models

class studentData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    course=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=100)
    
