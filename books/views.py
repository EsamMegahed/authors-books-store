from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from django.contrib import messages
from . models import Author
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    
class AuthorsListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name',]

    def form_valid(self, form) -> HttpResponse:
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'the author has been added '
        )
        return super().form_valid(form)