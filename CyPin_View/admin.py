from django.contrib import admin

from .models import Items, Issues, Stocks
# Register your models here.
admin.site.register(Items)
admin.site.register(Issues)
admin.site.register(Stocks)
