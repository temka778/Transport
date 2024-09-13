from django.contrib import admin
from .models import Technique, TechniquePhoto


class TechniquePhotoInline(admin.TabularInline):
    model = TechniquePhoto
    extra = 1


class TechniqueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Technique._meta.fields]
    inlines = [TechniquePhotoInline]


admin.site.register(Technique, TechniqueAdmin)
