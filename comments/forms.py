#!/user/bin/env python
# !-*-coding:utf-8 -*-
# !@Time     :2018/6/10 13:30
# !@Author   :sizhou
# !@File     :.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','content']