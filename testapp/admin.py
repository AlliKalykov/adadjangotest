from django.contrib import admin
from .models import ModelName, SecondModel


class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("id", "name_string", "age_int", "email_string", "float_number", "created_at", "updated_at", "birthday", "text")
    list_display_links = ("id", "name_string")


class SecondModelAdmin(admin.ModelAdmin):
    list_display = ("id", "model_name", "first", "second", "third", "four", "six", "seven", "eight", "nine")
    list_display_links = ("id", "model_name")

admin.site.register(ModelName, ModelNameAdmin)
admin.site.register(SecondModel, SecondModelAdmin)
