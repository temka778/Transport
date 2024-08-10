from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'phone_number', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)