from django.contrib import admin
from .models import AuthUser, Skill

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender')

admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(Skill)
