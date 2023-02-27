from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Has classes that represent tables in database

class Entry(models.Model):
    #attributes
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{} '.format(self.id)

    #Manages spelling
    class Meta():
        verbose_name_plural = 'entries'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username