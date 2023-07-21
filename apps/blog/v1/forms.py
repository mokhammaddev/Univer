from django import forms
from apps.blog.models import Comment
from ...main.models import Subscribe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            "class": "form-control",
            "id": "body",
            "name": "body",
            "cols": "30",
            "rows": '10',
        })
