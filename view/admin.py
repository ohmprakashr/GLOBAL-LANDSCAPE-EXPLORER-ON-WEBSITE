from django.contrib import admin
from .models import *

class collectionAdmin(admin.ModelAdmin):
    list_display =('name', 'image', 'description')

admin.site.register(collection,collectionAdmin)
admin.site.register(places)
