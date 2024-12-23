from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views import generic


class UserRegister(generic.CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        login(self.request, form.save())
        return redirect("blog:post-list")
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:post-list')
        return super().dispatch(*args, **kwargs)
    

class UserLogin(LoginView):
    template_name = "users/login.html"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:post-list')
        return super().dispatch(*args, **kwargs)
    

class UserLogout(LogoutView):
    pass




