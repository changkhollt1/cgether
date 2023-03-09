from django import forms
from .models import Comment
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



class RegistrationForm(forms.Form):
    username = forms.CharField(label="Tai Khoan:", max_length=30)
    email = forms.EmailField(label="emai:")
    password1 = forms.CharField(label="mat khau:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="nhap lai mat khau:", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1==password2 and password1:
                return password2
            raise forms.ValidationError("mat khau khong hop le")
    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("ten tai khoan co ki tu dac biet")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("tai khoan da ton tai")
    def save(self):
        username_post = self.cleaned_data['username']
        email_post = self.cleaned_data['email']
        password_post = self.cleaned_data['password1']
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.order = self.order
        comment.save()
    
    class Meta:
        model = Comment
        fields = ['body']

