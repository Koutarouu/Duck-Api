from django.contrib import admin
from .models import Animals
# Register your models here.
@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'last_name')