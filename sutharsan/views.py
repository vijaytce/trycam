from django.shortcuts import render

def cam(request):
    return render(request, 'index.html')