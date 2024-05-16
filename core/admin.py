from django.contrib import admin
from .models import Item,Category


admin.site.register(Category)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['category','media','text','img']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['img','name']


admin.site.register(Item,ItemAdmin)