from django import forms
from django.shortcuts import get_object_or_404
from .models import Comment , Blog



class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['write_a_comment','name','email']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image','title', 'description','category','active']

    def save(self, commit=True, user=None):
        blog = super().save(commit=False)
        if user:
            blog.owner = user 
        if commit:
            blog.save()
        return blog