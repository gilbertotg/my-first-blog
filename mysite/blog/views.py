from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post #El punto antes de models indica el directorio actual o la aplicación actual. Ambos, views.py y models.py están en el mismo directorio
from django.utils import timezone
from .forms import PostForm #incluye el forms.py para usarlo en post_new

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #lista de post publicados ordenados por published_date
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():  #para redirigir al detalle del post
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now() #se vera publicado
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
    return render(request, 'blog/post_edit.html', {'form': form})