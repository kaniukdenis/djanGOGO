# -*-coding: utf-8 -*-

from django.forms import ModelForm
from public.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
