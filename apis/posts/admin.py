from django.contrib import admin
from apis.posts.models import Post, Comment

# Register your models here.

admin.site.site_header = "admin site SITE HEADER"
admin.site.site_title = "admin site SITE TITLE"
admin.site.index_title = "admin site SITE INDEX"


# admin.site.register(Posts)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title','created_at')

    search_fields = ('title',)

    list_filter = ('created_at',)

    ordering = ('-created_at',)

    list_display_links = None

    list_editable = ('title',)

    list_per_page = 2

admin.site.register(Posts, PostAdmin)
