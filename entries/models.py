from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Entries"