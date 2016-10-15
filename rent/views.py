from django.shortcuts import render
from django.http import HttpResponse
from  .models import Monrent
# Create your views here.

def index(request):
    rent_list = Monrent.objects.order_by('id')
    output = ','.join([r.title for r in rent_list])
    template = loader.get_template('rent/index.html')
    context = {'properties for rent': rent_list,
              }
    #return HttpResponse("hello, proj monrent rent app")
    return HttpResponse(template.render(context,request))

def detail(request,monrent_id):
    return HttpReponse("This is the detail page%s." % monrent_id)
