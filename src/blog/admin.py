from django.contrib import admin

from blog.models import Category, BlogPost


# 1. facon de le faire
# Register your models here.
# admin.site.register(Category)
# admin.site.register(BlogPost)

# 2. facon en passant par une classe
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'author', 'date', 'world_count')
    empty_value_display = 'Inconnue'

    list_display_links = ('date', )
    list_editable = ('published', 'title', )
    search_fields = ('title', )
    list_filter = ('published', 'author', )
    autocomplete_fields = ('author', )
    list_per_page = 3