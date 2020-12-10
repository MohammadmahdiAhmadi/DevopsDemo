from django.urls import path

from . import views
from .views import(
    IdeaListView,
    IdeaDetailView,
    IdeaCreateView,
    IdeaUpdateView
)


urlpatterns = [
    path('', IdeaListView.as_view(), name = 'home'),
    path('idea/<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
    path('idea/new', IdeaCreateView.as_view(), name='idea-create'),
    path('idea/<int:pk>/update', IdeaUpdateView.as_view(), name='idea-update'),
    path('about/', views.about, name = 'about'),
]