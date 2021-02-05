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

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']
    paginate_by = 10


class IdeaDetailView(DetailView):
    model = Idea

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Idea, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['idea_is_liked'] = liked
        return data


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


@login_required
def likeIdea(request):
    if request.method == 'GET':

        idea_id = request.GET['idea_id']
        likedidea = Idea.objects.get(pk=idea_id) #getting the liked idea

        if likedidea.likes.filter(id=request.user.id).exists():
            likedidea.likes.remove(request.user)
        else:
            likedidea.likes.add(request.user)
                
        return HttpResponse(likedidea.number_of_likes()) # Sending an success response

    else:
        return HttpResponse("Request method is not a GET")
