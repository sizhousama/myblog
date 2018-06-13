from django.contrib import admin

# Register your models here.

from .models import Category,Tag
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','theme_img','title','summary','content','update_time','category','author')
    search_fields = ('title','create_time','update_time','category')
    #list_filter
    #ordering = ()
    fields = ('theme_img','title','author','summary','content','category','tags')


admin.site.register(Category)
admin.site.register(Tag)

