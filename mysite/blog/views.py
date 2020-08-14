from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post #El punto antes de models indica el directorio actual o la aplicación actual. Ambos, views.py y models.py están en el mismo directorio
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #lista de post publicados ordenados por published_date
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})