from django.contrib import admin

# Register your models here.
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','url','content','created_time')
    search_fields = ('name', 'created_time')
    # list_filter
    # ordering = ()
    exclude = ['created_time']



