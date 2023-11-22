from django.shortcuts import render
from django.views import generic

from .models import Post



class PostListView(generic.ListView):
    queryset = Post.objects.filter(active=True)
    template_name = 'post/postlist.html'
    context_object_name = 'post_detail'
