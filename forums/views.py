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