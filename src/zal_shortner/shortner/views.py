from django.shortcuts import render, get_object_or_404, redirect

from shortner.models import ShortenedURL

def home_page(request):
    recent_links = ShortenedURL.objects.order_by("-created_at")[:2]

    if request.method == "GET":
        return render(request, "shortner/index.html", {"recent_links": recent_links})

    url = request.POST.get("url")
    if not url:
        return render(request, "shortner/index.html", {"error": "Invalid URL", "recent_links": recent_links})
    
    s = ShortenedURL(main_url=url)
    s.save()

    return render(request, "shortner/result.html", {"url": s})
   
def result(request):
    return render(request, "shortner/result.html", {})


def redirect_view(request, pk):
    s = get_object_or_404(ShortenedURL, pk=pk)
    s.track_unique_visit(request)
    return redirect(s.main_url)


def dashboard(request, pk):
    s = get_object_or_404(ShortenedURL, pk=pk)
    return render(request, "shortner/result.html", {"url": s})

