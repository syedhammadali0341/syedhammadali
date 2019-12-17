from django import forms
from .models import Snippet
from crispy_forms .helper import FormHelper


class Info(forms.Form):
#     helper = FormHelper()
#     helper.Form_show_labels = False
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    description = forms.CharField(max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!')


    source = forms.CharField(  # A hidden input for internal use
        max_length=50,  # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )
    # image = forms.ImageField()


def clean(self):
    cleaned_data = super(Info, self).clean()
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')
    description = cleaned_data.get('description')
    if not name and not email and not description:
        raise forms.ValidationError('You have to write something!')


class SnippetForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.Form_show_labels = False

    class Meta:
        model = Snippet
        fields = ("name", "email", "description")
