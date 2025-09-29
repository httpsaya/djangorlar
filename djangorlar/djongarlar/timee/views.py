from django.shortcuts import render
from datetime import datetime
import pytz

timezones = {
    'Calgary': 'America/Edmonton',
    'Moscow': 'Europe/Moscow',
    'Almaty': 'Asia/Almaty'
}

def render_time(request):
    selected_city = request.GET.get('city')
    current_time = None
    if selected_city in timezones:
        tz = pytz.timezone(timezones[selected_city])
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'city-time/time.html', {
        'cities': timezones.keys(),
        'selected_city': selected_city,
        'current_time': current_time,
    })
