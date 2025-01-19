
from django.db import models
from django.contrib import admin
from django.forms import Textarea
from .models import Movie, Director, Actor, Screenwriter, Category,ProductionCompany,Country


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_title', 'release_year', 'imdb_score', 'short_description', 'image_preview', 'duration', 'country_list', 'production_company_list')
    search_fields = ('title', 'original_title', 'description')
    list_filter = ('release_year', 'imdb_score')
    filter_horizontal = ('directors', 'actors', 'screenwriters', 'categories', 'countries', 'production_companies')

    fieldsets = (
        (None, {
            'fields': ('title', 'original_title', 'description', 'imdb_score', 'release_year', 'image', 'iframe_url', 'duration')
        }),
        ('Relationships', {
            'fields': ('directors', 'actors', 'screenwriters', 'categories', 'countries', 'production_companies')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 60})},
    }

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;">'
        return "No image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"

    def country_list(self, obj):
        return ", ".join([country.name for country in obj.countries.all()])
    country_list.short_description = "Countries"

    def production_company_list(self, obj):
        return ", ".join([company.name for company in obj.production_companies.all()])
    production_company_list.short_description = "Production Companies"

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Screenwriter)
class ScreenwriterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize columns shown in the admin page
    search_fields = ('name',)  # Add a search bar for filtering countries
    ordering = ('name',)  # Order countries alphabetically

@admin.register(ProductionCompany)
class ProductionCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize columns shown in the admin page
    search_fields = ('name',)  # Add a search bar for filtering production companies
    ordering = ('name',)  # Order production companies alphabetically
