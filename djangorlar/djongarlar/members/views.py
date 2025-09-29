from django.shortcuts import render
context = {
    'users': [
        {
            'id': 1,
            'name': 'Zhansaya',
            'surname': 'Umirkulova',
            'age': '19',
        },
        {
            'id': 2,
            'name': 'Aiym',
            'surname': 'Satybaldy',
            'age': '19',
        },
        {
            'id': 3,
            'name': 'Miras',
            'surname': 'Kairat',
            'age': '20',
        },
        {
            'id': 4,
            'name': 'Dias',
            'surname': 'Tamirlan',
            'age': '23',
        },
        {
            'id': 5,
            'name': 'Aidana',
            'surname': 'Alieva',
            'age': '18',
        },
    ]
}
def render_users(request):
    return render(request,'users/user.html', context)

def render_user(request, id):
    user = next((e for e in context['users'] if e['id'] == id), None)
    return render(request, 'users/users.html', {'user': user})