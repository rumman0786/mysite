from django.shortcuts import render
import sys
from django.http import HttpResponse
from usermodule.forms import UsermoduleProfileForm
# Create your views here.
def index(request):
	form = UsermoduleProfileForm()
	return render(request, 'usermodule/index.html', {
            'form': form,
        })