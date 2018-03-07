from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models, stores, dummy_data

members_store = stores.MemberStore()
posts_store = stores.PostStore()
dummy_data.seed_stores(members_store, posts_store)

def index(request):
    context = {
        'posts': posts_store.get_all()
    }
    return render(request, 'index.html', context)

def topic_add(request):
    if request.method == "POST":
        new_post = models.Post(request.POST["title"], request.POST["content"])
        posts_store.add(new_post)
        return redirect('index')
    else:
        return render(request, 'topic_add.html')

def topic_show(request, id):
    context = {
        'post': posts_store.get_by_id(id)
    }
    return render(request, 'topic_show.html', context)

def topic_edit(request, id):
    post = posts_store.get_by_id(id)
    context = {
        'post': post
    }
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        posts_store.update(post)
        return render(request, 'topic_show.html', context)
    else:
        return render(request, 'topic_edit.html', context)

def topic_delete(request, id):
    posts_store.delete(id)
    return redirect('index')