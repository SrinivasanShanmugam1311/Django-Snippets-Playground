from django.shortcuts import render

# Create your views here.
def show_wp(request):
    return render(request,'wp.html')

# Create your views here.
def show_themes(request):
    return render(request,'themes.html')