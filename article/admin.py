from django.contrib import admin
from .models import Article, BlogType


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title", "content","author","created_time","last_updated_time","blog_type","views")
    ordering = ("id",)  # 按id正排序
    # ordering = ("-id",)   # 按id逆排序



# admin.site.register(Article, ArticleAdmin)