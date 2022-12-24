from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.TextField()
    phone=models.CharField(max_length=10)
    city=models.TextField()
    state=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name





