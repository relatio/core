from django.views.generics import DetailView

from . import models


class PersonView(DetailView):
    model = models.Person
