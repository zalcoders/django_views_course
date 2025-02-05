from django.shortcuts import render


def password_generator_view(request):
    return render(request, "main/index.html", {})
