from django.db import models
import os

# Create your models here.
class Result(models.Model):
    result_no = models.IntegerField()
    result_url = models.ImageField(upload_to='cari/images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)