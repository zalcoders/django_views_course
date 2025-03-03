from django.shortcuts import render
from contact_us.models import ContactRequest


def home(request):
    if request.method == "POST":
        data = request.POST
        attachment = None
        if "attachment" in request.FILES:
            attachment = request.FILES["attachment"]

        cr = ContactRequest(
            name=data["name"],
            gamer_tag=data["gamer_tag"],
            email=data["email"],
            subject=data["subject"],
            attachment=attachment,
            message=data["message"],
        )
        cr.save()
    return render(request, "contact_us/index.html", {})
