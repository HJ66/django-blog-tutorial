from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta(object):
		model = Comment
		fields = ['name', 'email', 'url', 'text']			
		