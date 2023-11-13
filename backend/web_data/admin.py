from django.contrib import admin
from .models import WebData

# Register your models here.
@admin.register(WebData)
class WebDataAdmin(admin.ModelAdmin):
    list_display =["id","username","first_name","last_name","email_id","phone_number","gender"]
