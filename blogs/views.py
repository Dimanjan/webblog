from .models import Post
from django.shortcuts import render

def PostList(request):
	post_list = Post.objects.filter(status=1).order_by('-created_on')
	context = {
		'post_list':post_list,
	}
	return render(request, 'home.html',context=context)

def PostDetail(request,slug):
	blog = Post.objects.get(slug=slug)
	top_content=blog.top
	focus_content=blog.focus
	bottom_content=blog.bottom
	date=blog.created_on
	context = {
		'blog':blog,
		'top_content':top_content,
		'focus_content':focus_content,
		'bottom_content':bottom_content,
		'date':date,
	}

	return render(request, 'blog_content.html',context=context)

