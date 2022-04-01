from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author',)
    search_fields = ('author', 'title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)