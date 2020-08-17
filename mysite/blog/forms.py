from django import forms

from .models import Post, Comment  #importamos modelos

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):  #formulario pra escribir un comentario
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)