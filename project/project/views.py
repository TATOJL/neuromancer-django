from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')    
def stock(request):
    return render(request, 'stock.html')  
def content(request):
    return render(request, 'content.html')  
