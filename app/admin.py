from django.contrib import admin

from .models import Target

# Register your models here.
@admin.register(Target)
class Target(admin.ModelAdmin):
    pass
