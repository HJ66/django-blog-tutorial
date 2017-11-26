from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
		

# 在Admin后台注册模型
# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

