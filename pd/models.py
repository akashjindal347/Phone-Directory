from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class record(models.Model):
    name=models.CharField(max_length=20)
    phone=models.DecimalField(decimal_places=0,max_digits=10)

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse('record_detail', args=[str(self.id)])
