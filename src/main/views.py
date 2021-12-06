from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, UpdateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('main:homepage')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('main:login')

def home_page(request):
    return render(request, 'main/home.html')

def registrationchoice_page(request):
    return render(request, 'main/registrationchoice.html')

def customerregister_page(request):
    if request.method!= 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.image = 'default.jpg'
            user.profile.iscustomer = True
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('main:login')
        else:
            print(form.errors)
    return render(request, 'main/customerregister.html', {'form': form})

def sellerregister_page(request):
    if request.method!= 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.image = 'default.jpg'
            user.profile.isseller = True
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('main:login')
        else:
            print(form.errors)
    return render(request, 'main/sellerregister.html', {'form': form})

def usereditview_page(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/home')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'main/edit_profile.html', {'user_form': user_form})

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'main/password-change.html'
    
def MyPasswordResetDoneView(request):
    return render(request, 'main/password-reset-done.html')
    