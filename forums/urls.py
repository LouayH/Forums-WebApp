from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'topic/add', views.topic_add, name='topic_add'),
    path(r'topic/<int:id>', views.topic_show, name='topic_show'),
]