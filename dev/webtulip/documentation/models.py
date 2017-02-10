from django.db import models

# Create your models here.


class Network(models.Model):
    name = models.CharField(max_length=255, blank=True)
    network = models.FileField(upload_to='networks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
