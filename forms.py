from django import forms

from .models import Post, Comment
#form for new post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
#form for comment
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)    
