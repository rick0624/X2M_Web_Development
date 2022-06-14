from django.db import models
from django.utils import timezone

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    keyword = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date  = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=50,blank = False,null = False) 
    last_name = models.CharField(max_length=50,blank = False,null = False)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank = False,null = False)
    message = models.TextField(max_length=10000,blank = False,null = False)

    def __str__(self):
        return self.first_name