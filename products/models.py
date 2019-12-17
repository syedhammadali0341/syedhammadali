from django.db import models


# Create your models here.
# description = models.CharField(max_length=255)
# class Snippet(models.Model):
#     name = models.CharField(max_length=255 )
#     email = models.EmailField(max_length=255)
#     description = models.TextField(max_length=255)
    # image = models.ImageField(default="default.jpg")
class Snippet(models.Model):
#     helper = FormHelper()
#     helper.Form_show_labels = False
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=255)
    # description = models.CharField(max_length=2000,
    #     widget=models.Textarea(),
    #     help_text='Write here your message!')

    #
    # source = models.CharField(  # A hidden input for internal use
    #     max_length=50,  # tell from which page the user sent the message
    #     widget=models.HiddenInput()
    # )
    # image = forms.ImageField()

def clean(self):
    cleaned_data = super(Snippet, self).clean()
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')
    description = cleaned_data.get('description')
    if not name and not email and not description:
        raise models.ValidationError('You have to write something!')


    def __str__(self):
        return f'{self.name}'