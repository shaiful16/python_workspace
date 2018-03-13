from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the hiya index.")

def getAge(request):
    print(request.GET["id"])
    print(request.GET["abcd"])
    return HttpResponse("hiya age is 20")

def getheight(request):
    return HttpResponse("hiya height is 6 feet")