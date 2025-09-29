from django.shortcuts import render

def render_count(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if request.method == 'POST':
        action = request.POST.get("action")
        if action == "click":
            request.session['count'] += 1
        elif action == "reset":
            request.session['count'] = 0
    return render(request, 'count/count.html', {'result': request.session["count"]})

