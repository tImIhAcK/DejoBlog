from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'category')
    list_filter = ('author', 'publish', 'status', 'category')
    search_fields= ('title',)
    prepopulated_fields= {'slug': ('title',)}
    raw_id_fields= ('author',)
    date_hierarchy= 'publish'
    ordering= ('status', 'publish')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')