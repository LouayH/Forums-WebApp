import json, random
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from . import models, stores

members_store = stores.MemberStore()
posts_store = stores.PostStore()

def index(request):
    context = {
        'posts': posts_store.get_all()
    }
    return render(request, 'index.html', context)

def topic_show(request, id):
    post = posts_store.get_by_id(id)
    if post:
        context = {
            'post': post
        }
        return render(request, 'topic_show.html', context)
    else:
        return HttpResponse("Not Found")

def topic_add(request):
    if request.method == "POST":
        new_post = models.Post(request.POST["title"], request.POST["content"])
        posts_store.add(new_post)
        return redirect('index')
    else:
        return render(request, 'topic_add.html')

def topic_edit(request, id):
    post = posts_store.get_by_id(id)
    if post:
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
    else:
        return HttpResponse("Not Found")

def topic_delete(request, id):
    post = posts_store.get_by_id(id)
    if post:
        posts_store.delete(id)
        return redirect('index')
    else:
        return HttpResponse("Not Found")


def api_topic_all(request):
    posts = [post.as_dict() for post in posts_store.get_posts_by_date()]
    return JsonResponse(posts, safe=False)

def api_topic_show(request,id):
    post = posts_store.get_by_id(id)
    if post:
        return JsonResponse(post.as_dict(), safe=False)
    else:
        return HttpResponse("Not Found")

@csrf_exempt
def api_topic_add(request):
    if request.method == "POST":
        id = random.choice(models.Member.objects.all()).id
        data = request.body.decode('utf-8')
        data = json.loads(data)
        new_post = models.Post(title=data["title"], content=data["content"], member_id=id)
        posts_store.add(new_post)
        return JsonResponse(new_post.as_dict())

@csrf_exempt
def api_topic_edit(request, id):
    if request.method == "PUT":
        post = posts_store.get_by_id(id)
        if post:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            post.title = data["title"]
            post.content = data["content"]
            posts_store.update(post)
            return JsonResponse(post.as_dict())
        else:
            return HttpResponse("Not Found")

@csrf_exempt
def api_topic_delete(request, id):
    if request.method == "DEL":
        post = posts_store.get_by_id(id)
        if post:
            posts_store.delete(id)
            return HttpResponse()
