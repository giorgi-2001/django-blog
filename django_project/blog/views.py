from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = "-created_at"
    paginate_by = 5


class UserPosts(generic.ListView):
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs.get("author")
        author = User.objects.get(username=username)
        return Post.objects.filter(author=author).order_by("-created_at").all()


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