from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})