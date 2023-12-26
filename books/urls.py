from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('authors/',views.AuthorsListView.as_view(),name='authors'),
    path('authors/add/',views.AuthorCreateView.as_view(),name='add_authors'),
    path('authors/<int:pk>/',views.AuthorDetailView.as_view(),name='authors_detail'),
]