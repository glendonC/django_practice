from django.contrib import admin
from .models import Entry, UserProfile

# Register your models here.
admin.site.register(Entry)
admin.site.register(UserProfile)
