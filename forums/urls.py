from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topic/<int:id>', views.topic_show, name='topic_show'),
    path(r'topic/add', views.topic_add, name='topic_add'),
    path(r'topic/edit/<int:id>', views.topic_edit, name='topic_edit'),
    path(r'topic/delete/<int:id>', views.topic_delete, name='topic_delete'),
    path(r'api/topic/all', views.api_topic_all, name="api_topic_all"),
    path(r'api/topic/<int:id>', views.api_topic_show, name="api_topic_show"),
    path(r'api/topic/add', views.api_topic_add, name="api_topic_add"),
    path(r'api/topic/edit/<int:id>', views.api_topic_edit, name="api_topic_edit"),
    path(r'api/topic/delete/<int:id>', views.api_topic_delete, name="api_topic_delete"),
]