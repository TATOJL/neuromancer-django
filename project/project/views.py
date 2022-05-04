from django.shortcuts import render


def hello(request):
    return render(request, 'index.html', {
        'content': "Hello Django ",
    })
def login(request):
    return render(request, 'login.html', {
        'content': "Hello Django ",
    })
def signup(request):
    return render(request, 'signup.html', {
        'content': "Hello Django ",
    })    
def stock(request):
    return render(request, 'stock.html', {
        'content': "Hello Django ",
    })  