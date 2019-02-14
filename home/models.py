from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone
# Create your models here.


class Posting(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(max_length=5000)
    gambar = models.ImageField(upload_to='upload')
    jadwal_publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.judul
