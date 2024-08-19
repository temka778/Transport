from django.contrib import admin
from .models import Technique


class TechniqueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Technique._meta.fields]


admin.site.register(Technique, TechniqueAdmin)