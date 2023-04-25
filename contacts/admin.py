from django.contrib import admin
from . import models

@admin.register(models.Individual)
class PersonalContact(admin.ModelAdmin):
    list_display=[
        'contact',
    ]

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'number',
        'email',
    ]
# Register your models here.
