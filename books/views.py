from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView,DetailView,FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.urls import reverse
from . models import Author
from . forms import AuthorBooksformset
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    
class AuthorsListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'auther_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name',]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'the author has been added'
        )
        return super().form_valid(form)
    


class AuthorbooksEditView(SingleObjectMixin,FormView):

    model = Author
    template_name = 'author_books_edit.html'

    def get(self,request,*args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request,*args, **kwargs)
    def get_form(self, form_class=None):
        return AuthorBooksformset(**self.get_form_kwargs(),instance=self.object)
    def get_success_url(self):
        return reverse('books:authors_detail',kwargs={'pk':self.object.pk})
    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'change were saved'
        )
        
        return HttpResponseRedirect(self.get_success_url())
    
    