from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','amount','description']

admin.site.register(Item,ItemAdmin)