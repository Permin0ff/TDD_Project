from django.db import models


class Catalog(models.Model):
    STATUS_CHOICES = (
        ('true', 'True'),
        ('false', 'False'),
    )

    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=5, choices=STATUS_CHOICES, default='false')

    def __str__(self):
        return self.title
