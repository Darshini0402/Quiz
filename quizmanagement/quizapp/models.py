from django.db import models

# Create your models here.

class quiz(models.Model):
    quesno=models.IntegerField(primary_key=True)
    question=models.CharField(max_length=200)
    a=models.CharField(max_length=200)
    b=models.CharField(max_length=200)
    c=models.CharField(max_length=200)
    d=models.CharField(max_length=200)
    ans=models.CharField(max_length=200)
    
    def __str__(self):
        return f" {self.quesno}"