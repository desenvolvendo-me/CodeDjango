from django.http import JsonResponse
from django.shortcuts import render

def hello(request):
    message = "Hello, World!"

    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({'message': message})
    else:
        return render(request, 'hello_app/hello.html', {'message': message})
