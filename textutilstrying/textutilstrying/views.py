from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")


def analyze(request):
    # get the text
    djtext = request.POST.get("text")
    print(djtext)
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps",'off')


    if removepunc == "on":
        punctuations = '''  !~@#$%^&*()_-+={}[]:;'<>?,./|\'""'';  '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed


    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed

    if removepunc == "off" and fullcaps == "off":
        return HttpResponse("SELECT ATLEAST ONE OPERATION")
    params = {"purpose" : "Your Text Has Been Analyzed" , "analyzed_text" : djtext}
    return render(request , "analyzed.html" , params)

def aboutme(request):
    return render(request , "about.html")


