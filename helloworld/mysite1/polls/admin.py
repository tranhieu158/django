from django.contrib import admin
from .models import choice, question
# Register your models here.
admin.site.register(question)
admin.site.register(choice)