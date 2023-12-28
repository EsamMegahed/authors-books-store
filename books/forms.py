from django.forms.models import inlineformset_factory
from .models import Author ,Book


AuthorBooksformset = inlineformset_factory(Author ,Book,fields=('title',))