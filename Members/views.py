from django.shortcuts import render,get_object_or_404
from django.views import generic 
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm,EditProfileForm,CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,CreateView
from theblog.models import UserProfile,Post
from django.contrib import messages
from django.contrib.auth.views import LoginView

class CreateProfilePageView(CreateView):
    model=UserProfile
    template_name='registration/create_profile.html'
    form_class=CreateProfileForm

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class UserRegisterView(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! You can now log in.')
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                if field == '__all__':
                    messages.error(self.request, error)
                else:
                    messages.error(self.request, f"{form.fields[field].label}: {error}")
        return super().form_invalid(form)


class ShowProfilePageView(DetailView):
    model=UserProfile
    template_name='registration/user_profile.html'

    
    def get_context_data(self, *args,**kwargs):
        
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(UserProfile,id=self.kwargs['pk'])
        user_post=Post.objects.filter(author=page_user.user)
        
        context={
            "page_user":page_user,
            "user_post":user_post,

        }
        return context


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html',{})

class EditProfilePageView(generic.UpdateView):
    model=UserProfile
    template_name='registration/edit_profile_page.html'
    fields=['bio','website_url','facebook_url','Linkedin_url','Instagram_url','profile_pic']
    success_url=reverse_lazy('home')



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)
