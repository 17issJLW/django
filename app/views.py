from django.shortcuts import render

# Create your views here.
from app import models
from django.shortcuts import HttpResponse
# Create your views here.

def db_handle(request):
    user_list_obj = models.pachong9.objects.all()
    return render(request,'t1.html',{'li':user_list_obj})