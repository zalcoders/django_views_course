from django.shortcuts import render
from django.http import Http404
import datetime as dt
from django.views.decorators.http import require_http_methods

import pytz

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
    if request.method == "POST":
        selected_timezone = request.POST.get("timezone", "")

        if not selected_timezone or selected_timezone not in ALLOWED_TIMEZONES:
            raise Http404("Time Zone Not Found!")
        
        request.session["timezone"] = selected_timezone

    selected_timezone = request.session.get("timezone", "UTC")

    timezone = pytz.timezone(selected_timezone)
    current_time = dt.datetime.now(timezone)

    context = {
        "current_dt": current_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "selected_timezone": selected_timezone,
        }
    response = render(request, "current_time/home.html", context)
    return response
