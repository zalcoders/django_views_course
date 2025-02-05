from django.shortcuts import render
from main.libs import generate_password

def password_generator_view(request):
    if request.method == "POST":
        length = int(request.POST.get("length"))
        uppercase = True if request.POST.get("uppercase") else False
        numbers = True if request.POST.get("numbers") else False
        symbols = True if request.POST.get("symbols") else False

        password, strength = generate_password(length, uppercase, numbers, symbols)

        return render(request, "main/result.html", {"password": password, "strength": strength})
    return render(request, "main/index.html", {})
