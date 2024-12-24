from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import generic
from .forms import UserUpdateForm, ProfileUpdateForm


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


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(
            data=request.POST,
            instance=request.user
        )
        p_form = ProfileUpdateForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect("users:profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "users/profile.html", context)
