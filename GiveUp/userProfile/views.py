from django.shortcuts import render, redirect
from .forms import NewRegistration, UserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from posts.views import default_home
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


# Create your views here.
def new_user_registration(request):

    if request.method == 'POST':
        form = NewRegistration(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message='Account - {} has been created'.format(username))
            return redirect(login_request)
    else:
        form = NewRegistration()

    return render(request=request, template_name='userProfile/registration.html', context={'form': form})


# Logins
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        next_value = request.POST.get('next')
        print(f'next_value is {next_value}')
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, message=f'your login attempt is successful')

                if next_value == "":
                    return redirect(default_home)
                else:
                    return redirect(f'{next_value}')
            else:
                messages.error(request, message=f'invalid username/password')

    else:
        form = AuthenticationForm()
    return render(request, template_name='userProfile/login.html', context={
        'form': form
        })


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.!')
    return redirect('login')


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':

        user_form = UserForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and userprofile_form.is_valid():
            user_form.save()
            userprofile_form.save()
            messages.success(request, message=f'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Please correct the error below. \n {user_form.errors} \n {userprofile_form.errors}')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, template_name='userProfile/profile.html', context={'user_form': user_form, 'userprofile_form':userprofile_form})


@login_required
def profile_view(request, username):
    # print(f'username is {username}')
    # userprofile = User.objects.get(username=username)
    userprofile_details = get_object_or_404(User, username=username)
    return render(request=request, template_name='userProfile/othersprofile.html', context={
        'userprofile_details': userprofile_details
    })