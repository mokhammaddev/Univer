from django import forms
from apps.main.models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control py-2",
            "type": "text",
            "id": "name",
        })
        self.fields['email'].widget.attrs.update({
            "class": "form-control py-2",
            "type": "email",
            "id": "email",
        })
        self.fields['body'].widget.attrs.update({
            "class": "form-control py-2",
            "type": "message",
            "id": "message",
            "rows": 8,
            "cols": 30,
        })


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            "class": "form-control email",
            "type": "email",
            "id": "email",
            "placeholder": "Enter email"
        })