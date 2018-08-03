from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.
def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post.reading_ratio=post.pk
    #request.POST.get(pk):
    post.reading_ratio += 1 #.update('int(post.reading_ratio += 1)') 
       # post.reading_ratio.update('int(post.reading_ratio)')   
    #else:
   # post.like_ratio+=1
    #post.dislike_ratio+=1
    
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

@csrf_exempt
def increase_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.like_ratio is None:
       post.like_ratio=0
    post.like_ratio +=1
    post.save()

    response_data ={}    
    response_data['result'] = 'success'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')
@csrf_exempt
def increase_dislike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.dislike_ratio is None:
       post.dislike_ratio=0
    post.dislike_ratio +=1 
    post.save()

    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form': form})
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)    

