from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render


# index = never_cache(TemplateView.as_view(template_name = 'index.html'))
def index (request) :
    return render(request,"/home/sandjon/Web/django/backend/build/index.html")
