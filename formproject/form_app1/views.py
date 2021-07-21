from django.shortcuts import render
from .forms import stud_form
# Create your views here.

def home(request):
    fm = stud_form
    return render(request,'home.html',{'form':fm})

