from django.http import HttpResponse


# Create your views here.
def SayHello(request):
    return HttpResponse("Hello Github Action")
