from django.shortcuts import render
from django.http import HttpResponse
# 导入数据模型
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import requests


# Create your views here.
def hello(request):
    return HttpResponse('Blog, Welcome!')


# 测试首页
def index1(request):
    sitename = 'Django中文网'
    url = 'www.django.com'
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型'
    ]
    mydict = {
        'name': 'Bill',
        'qq': 993538388,
        'wx': 'wyb_321',
        'email': '993538388@qq.com'
    }

    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all()

    # 把变量封装到上下文里
    context = {
        'sitename': sitename,
        'url': url,
        'list': list,
        'mydict': mydict,
        'allarticle': allarticle
    }
    # 把上下文传递到模板里
    return render(request, 'index.html', context)


# 全局函数
def global_variable(request):
    # 查询所有分类
    allcategory = Category.objects.all()
    # 查询所有标签
    tags = Tag.objects.all()
    # 查询友情链接
    links = Link.objects.all()
    # 查询热门推荐位文章10条
    tui_hot = Article.objects.filter(tui_id=2)[0:10]
    # 热门文章排行
    # hot = Article.objects.all().order_by('?')[0:10]   # 随机排行
    # hot = Article.objects.all().order_by('?')[0:10]   # 通过推荐进行查询，以推荐ID为3位例
    hot = Article.objects.all().order_by('views')[:10]  # 通过浏览数进行排序
    return locals()


# 首页
def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询并过筛选灯片数据
    tui = Article.objects.filter(tui_id=1)[0:3]  # 查询首页推荐位文章3条
    allarticle = Article.objects.all().order_by('-id')[0:10]  # 查询最新文章
    return render(request, 'index.html', locals())


# 列表页
def list(request, lid):
    # 获取通过URL传进来的lid，然后筛选出对应的文章
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名

    # 在URL中获取当前页面数
    page = request.GET.get('page')
    # 对查询到的数据对象list进行分页，设置超过5条数据进行分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时，显示第1页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页面不在系统的页面列表时，
        # 显示最后一页的内容
        list = paginator.page(paginator.num_pages)

    return render(request, 'list.html', locals())
    # locals()的作用是返回一个包含当前作用域里面的所有变量和他们的值得字典。


# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)
    random_tui = Article.objects.all().order_by('?')[:10]  # 随机推荐可能感兴趣的文章
    next_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    previous_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()

    return render(request, 'show.html', locals())


# 标签列表页
def tag(request, tag):
    # 获取通过URL传进来的lid，然后筛选出对应的文章
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)  # 获取当前文章的栏目名

    # 在URL中获取当前页面数
    page = request.GET.get('page')
    # 对查询到的数据对象list进行分页，设置超过5条数据进行分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时，显示第1页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页面不在系统的页面列表时，
        # 显示最后一页的内容
        list = paginator.page(paginator.num_pages)

    return render(request, 'tags.html', locals())
    # locals()的作用是返回一个包含当前作用域里面的所有变量和他们的值得字典。


# 搜索结果页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取搜索关键词通过标题进行匹配

    # 在URL中获取当前页面数
    page = request.GET.get('page')
    # 对查询到的数据对象list进行分页，设置超过5条数据进行分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时，显示第1页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页面不在系统的页面列表时，
        # 显示最后一页的内容
        list = paginator.page(paginator.num_pages)

    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())


