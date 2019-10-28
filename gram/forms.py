from django import forms
from django.contrib.auth.models import User
from insta.models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True,label='',widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}))
    first_name = forms.CharField(max_length=256,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=256,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username = forms.CharField(max_length=60,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    class Meta:
        model = User
        fields = ['email','first_name', 'last_name','username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio']
