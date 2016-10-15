from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from  .models import Monrent
# Create your views here.

def index(request):
    rent_list = Monrent.objects.order_by('id')[:10]
    #output = ','.join([r.title for r in rent_list])
    #template = loader.get_template('rent/index.html')
    context = {'properties for rent': rent_list
              }
    #return HttpResponse("hello, proj monrent rent app")
    #return HttpResponse(template.render(context,request))
    return render(request,'rent/index.html',context)

def detail(request,monrent_id):
    #try:
    #     properties = Monrent.objects.get(pk=monrent_id)
    #except properties.DoesNotExist:
    #     raise Http404("properties do not exist")
    #return HttpReponse("This is the detail page%s." % monrent_id)
    #return render(request, 'rent/detail.html',{'properties':properties})

    properties = get_object_or_404(Monrent,pk=id)
    return render(request,'rent/detail.html',{'properties':properties})
