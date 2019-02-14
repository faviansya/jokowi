from django.contrib import admin
from .models import Posting
# Register your models here.

postmentee = [Posting,]
admin.site.register(postmentee)