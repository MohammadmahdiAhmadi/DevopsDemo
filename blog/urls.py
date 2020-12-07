from django.urls import path

from . import views
from .views import(
    IdeaListView,
    IdeaDetailView,
)


urlpatterns = [
    path('', IdeaListView.as_view(), name = 'home'),
    path('idea/<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
    path('about/', views.about, name = 'about'),
]