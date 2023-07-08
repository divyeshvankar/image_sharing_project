from django.db import models

class Image(models.Model):
    binary_data = models.BinaryField()
