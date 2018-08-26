from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=30, default="N/A")
    item_model = models.CharField(max_length=30, default="N/A")
    item_cost = models.IntegerField(default=0)
    item_count = models.IntegerField(default=-1)
    item_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Items"

class Issues(models.Model):
    issue_name = models.CharField(max_length=30, default="N/A")
    issue_model = models.CharField(max_length=30, default="N/A")
    issue_count = models.IntegerField(default=0)
    isuue_to = models.CharField(max_length=50, default="N/A")
    issue_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Issues"

class Stocks(models.Model):
    stock_name = models.CharField(max_length=30, default="N/A")
    stock_model = models.CharField(max_length=30, default="N/A")
    stock_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Stocks"