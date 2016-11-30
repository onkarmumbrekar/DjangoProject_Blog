from django.db import models
from datetime import datetime
from django.contrib.auth.models import Permission, User

class blogmod(models.Model):
    user = models.ForeignKey(User, default=1)
    title=models.CharField(max_length=50)
    blog_text = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + '-' + self.blog_text