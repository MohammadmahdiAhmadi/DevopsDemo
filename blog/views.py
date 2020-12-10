from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Idea
from django.contrib.auth.models import User



class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']
    paginate_by = 10
    

class IdeaDetailView(DetailView):
    model = Idea


class IdeaCreateView(LoginRequiredMixin, CreateView):
    model = Idea
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IdeaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.author:
            return True
        return False


class IdeaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Idea
    success_url = '/'

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.author:
            return True
        return False


class UserIdeaListView(ListView):
    model = Idea
    template_name = 'blog/user_ideas.html'
    context_object_name = 'ideas'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Idea.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    