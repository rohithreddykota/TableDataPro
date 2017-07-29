from django.shortcuts import render

# Create your views here.


def openUI5(request):
    return render(request, 'tableproApp/webapp/index.html')
