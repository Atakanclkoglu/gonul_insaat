from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')  # 'content' alanını list_display'a ekledim
    search_fields = ('title', 'content')
    list_editable = ('content',)
    list_filter = ('created_at',)
