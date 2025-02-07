from django.shortcuts import render


def home_page(request):
    return render(request, "shortner/index.html", {})

def result(request):
    return render(request, "shortner/result.html", {})
