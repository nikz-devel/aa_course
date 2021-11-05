from decimal import Decimal

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    cost = models.DecimalField(default=Decimal("0.0"), decimal_places=2, max_digits=10)
    worker = models.ForeignKey("popug_auth.User", null=True, on_delete=models.CASCADE)
