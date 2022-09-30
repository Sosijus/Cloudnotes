from django.shortcuts import render

def reg(request):
    return render(request, "regpage.html")

def note(request):
    return render(request, "notevisual.html")

def log(request):
    return render(request, "logpage.html")