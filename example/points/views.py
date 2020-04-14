from django.views.generic.edit import CreateView, UpdateView

from .models import Place


class PlaceCreate(CreateView):
    model = Place
    fields = ['location']
    success_url = 'place_create'


class PlaceUpdate(UpdateView):
    model = Place
    fields = ['location']
    template_name_suffix = '_update_form'
