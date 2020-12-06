from django.shortcuts import render

from django.views.generic import(
    ListView,
    DetailView,
)



class IdeaListView(ListView):
    template_name = 'blog/home.html'

