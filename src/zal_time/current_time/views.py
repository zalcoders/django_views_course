from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, Http404
import datetime as dt
from django.views.decorators.http import require_http_methods

ALLOWED_TIMEZONES = [
    "UTC",
    "America/New_York",
    "America/Chicago",
    "America/Denver",
    "America/Los_Angeles",
    "Asia/Tokyo",
    "Asia/Tehran",
    "Europe/London",
    "Europe/Paris",
    "Asia/Dubai",
    "Asia/Singapore",
]

# @require_http_methods(["POST"])
def home(request):
    print(request.POST)
    if request.method == "POST":
        selected_timezone = request.POST.get("timezone", "")

        if not selected_timezone or selected_timezone not in ALLOWED_TIMEZONES:
            raise Http404("Time Zone Not Found!")

    context = {"current_dt": dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
    return render(request, "current_time/home.html", context)
