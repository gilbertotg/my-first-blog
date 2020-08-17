from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url # se agrega para  url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

urlpatterns = [
    path('', views.post_list, name='post_list'), #lias de de post
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #ver el detalle del post
    path('post/new', views.post_new, name='post_new'),   #agregar un nuevo post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), #editar un post
    path('drafts/', views.post_draft_list, name='post_draft_list'), #editar borradores
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]