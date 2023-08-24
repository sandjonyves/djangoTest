from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render,HttpResponse


# index = never_cache(TemplateView.as_view(template_name = '/home/sandjon/Web/django/backend/build/index.html'))
def index (request) :
    ct = {
        "fedfdfdf"
    }
    return HttpResponse('fdffdfdfdffddfdfd')
