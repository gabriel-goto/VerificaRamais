from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from Vramal.ramal.models import Ramal, pessoa

def post_list(request):
    return render(request, 'ramal/post_list.html', {})

def home(request):

	ramalv = Ramal.objects.all()

	pessoaa = pessoa.objects.all()

	template = loader.get_template('ramal/index.html')

	context = RequestContext(request, {'ramalv':ramalv})
	return HttpResponse(template.render(context))