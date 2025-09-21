from django.shortcuts import render

# Create your views here.

def bmi_html(request):
    return render(request, 'bmi.html')
