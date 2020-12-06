from django.shortcuts import render

from django.views.generic import(
    ListView,
    DetailView,
)
from .models import Idea



class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'

