from django.contrib import admin

# Register your models here.
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Fcuser, FcuserAdmin)