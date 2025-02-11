from django.shortcuts import render
import datetime as dt

def home(request):
    context = {
        "current_dt": dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    return render(request, "current_time/home.html", context)