from django.shortcuts import render

context = {
    'name': 'Saya',
    'users': 'users',
    'city_time': 'city-time',
    'cnt': 'cnt',
}

def index(request):
    return render(request, 'first/index.html', context)