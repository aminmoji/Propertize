from django.shortcuts import render, redirect
from .models import Property
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm, ShowingForm, CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {
        'properties': properties
    })


def about(request):
    return render(request, 'about.html')



def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'properties/detail.html', {
        'property': property
    })


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#        form = CustomUserCreationForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            login(request, user)
#            return redirect('index')
#        else:
#            error_message = 'Invalid Sign Up Attempt, Please Try Again.'

#     form = CustomUserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return redirect(request, 'signup.html', context)


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
  template_name = "add_property.html"

class PropertyDelete(LoginRequiredMixin, DeleteView):
  model = Property
  success_url = '/properties/'


@login_required
def add_showing(request, property_id):
    form = ShowingForm(request.POST)
    if form.is_valid():
        new_showing = form.save(commit=False)
        new_showing.property_id = property_id
        new_showing.save()
    return redirect('detail', property_id = property_id)

