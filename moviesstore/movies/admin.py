from django.contrib import admin
from .models import Movie , Review

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass