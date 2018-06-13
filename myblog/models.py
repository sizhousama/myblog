from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from DjangoUeditor.models import UEditorField


# Create your models here.
class Category(models.Model):
    c_name = models.CharField(u'分类',max_length=100)

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = 'Category'

class Tag(models.Model):
    t_name = models.CharField(u'主题标签', max_length=100, blank=True)

    def __str__(self):
        return self.t_name

    class Meta:
        db_table = 'Tag'


class Article(models.Model):
    theme_img = models.ImageField(u'主题图片',upload_to = 'img',blank=True)
    title = models.CharField(u'文章标题',max_length = 255)
    summary = models.CharField(u'摘要', max_length=255)
    content = UEditorField(u'文章内容',height=400,width=1120,default=u'',blank=True)
    create_time = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,editable=True)
    comment_data = models.PositiveIntegerField(u'评论数',default=0,blank=True)
    views = models.PositiveIntegerField(u'浏览量',default=0,blank=True)

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
            return self.content[:10]



    def get_absolute_url(self):
        return reverse('myblog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields = ['views'])


    class Meta:
        ordering = ['-create_time']
        db_table = 'Article'

