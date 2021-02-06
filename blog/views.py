from django.shortcuts import render, get_object_or_404, redirect

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

from .forms import CommentForm

class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']
    paginate_by = 5


# class IdeaDetailView(DetailView):
#     model = Idea

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         thisIdea = get_object_or_404(Idea, id=self.kwargs['pk'])

#         #Like button
#         liked = False
#         if thisIdea.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         data['number_of_likes'] = thisIdea.number_of_likes()
#         data['idea_is_liked'] = liked

#         return data


def IdeaDetailView(request, pk):
    template_name = 'blog/idea_detail.html'
    thisIdea = get_object_or_404(Idea, id=pk)

    #Comment
    comments = thisIdea.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.idea = thisIdea
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()


    #Like button
    liked = False
    if thisIdea.likes.filter(id=request.user.id).exists():
        liked = True
    
    #Counting views
    thisIdea.views = thisIdea.views + 1
    thisIdea.save()

    context = {
        'object': thisIdea,

        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,

        'number_of_likes': thisIdea.number_of_likes(),
        'idea_is_liked': liked
    }

    return render(request, template_name, context)


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


@login_required
def dislikeIdea(request):
    if request.method == 'GET':

        idea_id = request.GET['idea_id']
        dislikedidea = Idea.objects.get(pk=idea_id) #getting the liked idea

        if dislikedidea.dislikes.filter(id=request.user.id).exists():
            dislikedidea.dislikes.remove(request.user)
        else:
            dislikedidea.dislikes.add(request.user)
                
        return HttpResponse(dislikedidea.number_of_dislikes()) # Sending an success response

    else:
        return HttpResponse("Request method is not a GET")