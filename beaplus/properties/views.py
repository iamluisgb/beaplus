"""Properties views."""

# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

# Models
from beaplus.properties.models import Property

def index(request):
    """
    Probando
    """
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'home/index.html'
    )

class PropertyDetailView(LoginRequiredMixin, DetailView):
    """Return Property detail."""

    template_name = 'properties/detail.html'
    queryset = Property.objects.all()
    context_object_name = 'property'