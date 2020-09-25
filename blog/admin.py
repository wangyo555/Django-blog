from django.contrib import admin

# 导入需要管理的数据库表
from .models import Article, Banner, Category, Tag, Link, Tui


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里要显示的字段
    list_display = ('id', 'category', 'title', 'user', 'tui', 'views', 'created_time')
    # 自动分页条数
    list_per_page = 20
    # 后台数据列表排列方式
    ordering = ('-created_time',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')