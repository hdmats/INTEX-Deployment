from django.contrib import admin
from .models import condition, user, nutrient, journal_entry
# Register your models here.
admin.site.register(condition)
admin.site.register(user)
admin.site.register(nutrient)
admin.site.register(journal_entry)