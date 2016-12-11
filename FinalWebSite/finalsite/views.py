from django.shortcuts import render

def all(request):
    print(request.path_info.split('/').pop())
    return render(request,request.path_info.split('/').pop())

