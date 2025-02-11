from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    print(exception)
    return render(request, "general/404.html", {"message": str(exception)})
