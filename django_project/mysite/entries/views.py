from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm

# Create your views here.

#pass name of the template
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'


    entries = Entry.objects.order_by('-date_posted')
    context = {'entries': entries, 'username': username}
    return render(request, 'entries/index.html', context)

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    context = {'form':form}
    return render(request, 'entries/add.html', context)


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()


            username=form.cleaned_data.get('username')
            password =form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form=UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)
