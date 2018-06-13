from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from django.http import HttpResponse
# Create your views here.
from .models import Article
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'myblog/search.html', {'error_msg': error_msg})

    article_list = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'myblog/search.html', {'error_msg': error_msg,
                                                  'article_list': article_list})

def archives(request):
    articlelist = Article.objects.all()
    dates = Article.objects.datetimes('create_time','month', order='DESC')
    return render(request, 'myblog/archives.html', {'articlelist':articlelist,
        'dates': dates})





class IndexView(ListView):
    model = Article
    template_name = 'myblog/index.html'
    context_object_name = 'articleList'
    paginate_by = 3


#def index(request):
    #articleList = Article.objects.all().order_by('-create_time')
    #return render(request,'myblog/index.html',{"articleList":articleList})

class ArticelDetailView(DetailView):
    model = Article
    template_name = 'myblog/detail.html'
    context_object_name = 'article'

    def get(self,request,*args,**kwargs):
        response = super(ArticelDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response



    def get_context_data(self,**kwargs):
        context = super(ArticelDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()

        context.update({
            'form':form,
            'comment_list':comment_list,
        })
        return context




    '''
def detail(request,pk):
    article = get_object_or_404(Article, pk= pk)

    article.increase_views()
    form = CommentForm()
    # 获取这篇 article 下的全部评论
    comment_list = article.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'article': article,
               'form': form,
               'comment_list': comment_list,
               }
    return render(request, 'myblog/detail.html',context=context)
    '''

