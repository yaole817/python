from django.shortcuts import render

# Create your views here.
def login(request):
    context = { 'status' : "this site error" }
    return render(request, 'login.html', context)