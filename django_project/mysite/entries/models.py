from django.db import models

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
    