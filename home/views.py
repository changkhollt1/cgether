from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'html/home.html')
def cuoicorner(request):
    return render(request, 'html/cuoi_corner.html')
def about(request):
    return render(request, 'html/about.html')

# xu ly loi
def error404(request, exception):
    return render(request, 'html/error.html')
def error500(request):
    return render(request, 'html/error.html')
# tao tai khoan
def register_user(request):
    form = RegistrationForm() 
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "thanh cong")
            form.save()
            # return HttpResponseRedirect('/')

    return render(request, 'html/register_user.html', {'form' : form})
    