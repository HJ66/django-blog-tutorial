from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown

from comments.forms import CommentForm
from .models import Post, Category

def index(request):
	# return HttpResponse('欢迎访问我的博客首页')
	# return render(request, 'blog/index.html', context={
	# 		'title': '我的博客首页',
	# 		'welcome': '欢迎访问我的博客首页'
	# 	})
	# post_list = Post.objects.all().order_by('-create_time')
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body, extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			'markdown.extensions.toc',
		])
	form = CommentForm()
	# 获取这篇文章post下的全部评论
	comment_list = post.comment_set.all()
	# 将文章、表单、以及文章下的评论列表作为模版变量传给detail.html模版，以便渲染相应的数据
	context = {'post': post,
			   'form': form,
			   'comment_list': comment_list
			   }
	# return render(request, 'blog/detail.html', context={'post': post})
	return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
	post_list = Post.objects.filter(create_time__year=year,
									create_time__month=month
									)
	return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate)
	return render(request, 'blog/index.html', context={'post_list': post_list})

	




















