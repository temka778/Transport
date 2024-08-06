from django.contrib import admin
from .models import Technique

class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Technique, TechniqueAdmin)