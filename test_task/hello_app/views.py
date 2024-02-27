from django.http import HttpRequest
from django.shortcuts import render


def hello_view(request: HttpRequest):
    name_param = request.GET.get('name')
    message_param = request.GET.get('message')

    context = {
        'name': name_param,
        'message': message_param
    }
    
    return render(request, 'hello_app/main.html', context=context)


