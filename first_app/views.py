from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dictionary = { 'access_records': webpages_list }
  return render(request, 'first_app/index.html', context=date_dictionary)

  # my_dict = {'insert_me': 'Hello I am from views.py! Now I am coming from first_app directory'}
  # return render(request, 'first_app/index.html', context=my_dict)

def show(request):
  my_dict = {'insert_me': 'Hello I am from views.py! Now I am coming from first_app directory'}
  return render(request, 'first_app/show.html', context=my_dict)
