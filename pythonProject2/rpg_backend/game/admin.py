from django.contrib import admin
from .models import Character, Monster, Item


admin.site.register(Character)
admin.site.register(Monster)
admin.site.register(Item)