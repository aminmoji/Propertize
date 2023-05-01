from django.shortcuts import render, redirect
from .models import Property
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm


# Create your views here.
def home(request):
    return HttpResponse('')


def about(request):
    return render(request, 'about.html')

@login_required
def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'properties/detail.html', {
        'property': property
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('index')
       else:
           error_message = 'Invalid Sign Up Attempt, Please Try Again.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return redirect(request, 'registration/signup.html', context)

@login_required
def properties_index(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'properties/index.html', {
        'properties': properties
    })

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('property_detail', property_id=property.id)
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

class PropertyUpdate(LoginRequiredMixin, UpdateView):
  model = Property
  fields = '__all__'

class PropertyDelete(LoginRequiredMixin, DeleteView):
  model = Property
  success_url = '/properties/'


