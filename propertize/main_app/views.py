from django.shortcuts import render, redirect
from .models import Property, Showing, Favorite
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm, ShowingForm, CustomUserCreationForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {
        'properties': properties
    })


def about(request):
    print("hi")
    return render(request, 'about.html')



def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    showing_form = ShowingForm()
    is_favorite = Favorite.objects.filter(property=property, user=request.user).exists()
    owner = property.user_id
    return render(request, 'properties/detail.html', {
        'property': property,
        'owner': owner,
        'showing_form': showing_form,
        'is_favorite': is_favorite,
    })


@login_required
def add_showing(request, property_id):
    form = ShowingForm(request.POST)
    if form.is_valid():
        new_showing = form.save(commit=False)
        new_showing.property_id = property_id
        new_showing.user = request.user
        new_showing.save()
    return redirect('detail', property_id=property_id)


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"


def showing_list(request):
    all_showings = Showing.objects.filter(user=request.user)
    print(all_showings)
    return render(request, 'showing_list.html', {
        'showings': all_showings,
    })


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse('home')



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
    print("hi")
    return render(request, 'properties/index.html', {
        'properties': properties
    })


@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('detail', property_id=property.id)
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


class PropertyUpdate(LoginRequiredMixin, UpdateView):
  model = Property
  fields = ('title', 'price', 'description', 'address', 'bedroom', 'bathroom', 'sqf', 'type', 'images')
  template_name = "add_property.html"

class PropertyDelete(LoginRequiredMixin, DeleteView):
  model = Property
  success_url = '/properties/'


@login_required
def add_to_favorites(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, property=property)
    if created:
        messages.success(request, f"{property.title} has been added to your favorites.")
    else:
        messages.warning(request, f"{property.title} is already in your favorites.")
    return redirect('detail', property_id=property_id)


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites_list.html', {
        'favorites': favorites,
    })


@login_required
def delete_from_favorites(request, favorite_id):
    favorite = get_object_or_404(Favorite, pk=favorite_id, user=request.user)
    favorite.delete()
    return redirect('favorites_list')