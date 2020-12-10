from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
)
from .models import Idea



class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']
    paginate_by = 2
    

class IdeaDetailView(DetailView):
    model = Idea


class IdeaCreateView(LoginRequiredMixin, CreateView):
    model = Idea
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    

