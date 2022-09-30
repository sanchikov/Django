from django.core.exceptions import ValidationError
from django.forms import forms

from .models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text'
                  'description',
                  ]

def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "description": "Описание не может быть менее 20 символов."
            })
        name = cleaned_data.get("title")
        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )
        return cleaned_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title',
                  'text'
                  'description',
                  ]