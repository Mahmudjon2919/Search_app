from django.contrib import admin
from .models import Blogs




@admin.register(Blogs)
class BlogsModel(admin.ModelAdmin):
    list_display = ("id", "title", "content")