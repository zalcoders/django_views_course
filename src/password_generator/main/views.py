from django.shortcuts import render


def calculate_password(length, uppercase, numbers, symbols):
    print(length, uppercase, numbers, symbols)


def password_generator_view(request):
    if request.method == "POST":
        length = request.POST.get("length")
        uppercase = True if request.POST.get("uppercase") else False
        numbers = True if request.POST.get("numbers") else False
        symbols = True if request.POST.get("symbols") else False

        calculate_password(length, uppercase, numbers, symbols)
    else:
        pass
    return render(request, "main/index.html", {})
