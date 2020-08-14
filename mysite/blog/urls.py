from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'), #lias de de post
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #ver el detalle del post
    path('post/new', views.post_new, name='post_new'),   #agregar un nuevo post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), #editar un post
]