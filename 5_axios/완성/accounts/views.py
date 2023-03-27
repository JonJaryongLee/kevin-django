from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

# @require_POST
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         person = User.objects.get(pk=user_pk)
#         if person != request.user:
#             if person.followers.filter(pk=request.user.pk).exists():
#             # if request.user in person.followers.all():
#                 person.followers.remove(request.user)
#             else:
#                 person.followers.add(request.user)
#         return redirect('accounts:profile', person.username)
#     else:
#         return redirect('accounts:login') 

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
                is_followed = False
            else:
                person.followers.add(request.user)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
                'followings_count': person.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', person.username)
    else:
        return redirect('accounts:login')