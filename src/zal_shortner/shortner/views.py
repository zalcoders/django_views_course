from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from shortner.models import ShortenedURL

def home_page(request):
    if request.method == "GET":
        return render(request, "shortner/index.html", {})

    url = request.POST.get("url")
    if not url:
        return render(request, "shortner/index.html", {"error": "Invalid URL"})
    
    s = ShortenedURL(main_url=url)
    s.save()

    return render(request, "shortner/result.html", {"url": s})
   
def result(request):
    return render(request, "shortner/result.html", {})


def redirect_view(request, pk):
    s = get_object_or_404(ShortenedURL, pk=pk)
    return redirect(s.main_url)
