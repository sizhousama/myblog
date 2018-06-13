from django.shortcuts import render, get_object_or_404, redirect
from myblog.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comment
from .forms import CommentForm


def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)

        else:
            comment_list = article.comment_set.all()
            paginator = Paginator(comment_list, 4)
            page = request.GET.get('page')
            try:
                comments = paginator.page(page)
            except PageNotAnInteger:
                comments = paginator.page(1)
            except EmptyPage:
                comments = paginator.page(paginator.num_pages)
            context = {
                'article': article,
                'form': form,
                'comments': comments,
                    }
            return render(request, 'myblog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(article)