from django.shortcuts import render, redirect


def authenticate(func):
    def inner(request):
        if request.user.is_authenticated:
            return func(request)
        else:
            return redirect('sign_in')
    return inner
