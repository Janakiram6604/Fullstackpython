from django.db import models
from django.conf import settings
# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    cover=models.ImageField(upload_to='cover/',blank=True)
    description=models.TextField(blank=True)
    added_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )
