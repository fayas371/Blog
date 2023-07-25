from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import UserProfile

class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args ,**kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

class CreateProfileForm(forms.ModelForm):
    
    class Meta:
        model=UserProfile
        fields=('bio','profile_pic','website_url','facebook_url','Linkedin_url','Instagram_url')

        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control','rows':'4'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'Linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            
            'Instagram_url':forms.TextInput(attrs={'class':'form-control'}),

        }
