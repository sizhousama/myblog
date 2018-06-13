from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    content = models.TextField()

    # parent为该评论的父评论，所以第一个参数为'self',当为空时表示为第一层级的评论
    # 指定related_name='children'，这样可以父评论通过comment.children获取子评论，默认是通过comment.comment_set获取
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    article = models.ForeignKey('myblog.Article')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-created_time']
        db_table = 'comments'