from django.db import models
from django.utils.timezone import localtime

class Link(models.Model):
    ip_address = models.GenericIPAddressField()
    date_clicked = models.DateTimeField(auto_now_add=True)
