from django.shortcuts import render_to_response, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Article


# 文章详情页
def article_detail(request, article_id):
    # try:
    #     article = Article.objects.get(id = article_id)
    #     context = {}
    #     context['article_obj'] = article
    # except Article.DoesNotExist:
    #     raise Http404('页面不存在')
    # # return HttpResponse('文章标题：%s <br> 文章内容：%s' % (article.title, article.content))
    # # return render(request, 'article_detail.html', context)
    # return render_to_response('article_detail.html', context)

    article = get_object_or_404(Article, id = article_id)
    context = {}
    context['article_obj'] = article
    return render_to_response('article_detail.html', context)


# 文章列表
def article_list(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles
    return render_to_response('article_list.html', context)