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