from django.db import models

from django.contrib.auth.models import User

class books(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    # important_high = models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title