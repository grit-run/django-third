from django.shortcuts import render
from django.views.generic import TemplateView


# Function based view
def index_func(request):
    return render(request, 'func_view.html')


# Class based view
class index_class(TemplateView):
    template_name = 'class_view.html'
