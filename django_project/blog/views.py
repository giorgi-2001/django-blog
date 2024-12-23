from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(generic.ListView):
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "body", "slug"]
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ["title", "body", "slug"]
    template_name = "blog/post_update.html"

    def test_func(self):
        return self.request.user == self.get_object().author
    

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    fields = ["title", "body", "slug"]
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post-list")

    def test_func(self):
        return self.request.user == self.get_object().author