from django.http import HttpResponse


# Create your views here.
def SayHi(request):
    return HttpResponse("Hello Github Action")
