from django.contrib import admin
from authentication.models import User

# Register your models here.


class AuthAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "role")


admin.site.register(User, AuthAdmin)
