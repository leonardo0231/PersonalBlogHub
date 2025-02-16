from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "date_joined")
    ordering = ("date_joined", "username",)


admin.site.register(CustomUser, CustomUserAdmin)