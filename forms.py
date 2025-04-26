from django import forms
from .models import ProfileData

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = ['followers', 'following', 'bio', 'has_profile_photo', 'is_private']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
