from django.shortcuts import render
from django.http import JsonResponse
from . import templates
from microblogging.supabase_utils import fetch_from_supabase, insert_to_supabase
from users_app.models import User

def index(request):
    users = User.objects.all().values()
    context = {
        'users': users,
    } 
    return render(request, 'first_template.html', context)

def fetch_users(request):
    data = fetch_from_supabase('users')
    return JsonResponse(data, safe=False)

def insert_user(request):
    if request.method == 'POST':
        data = request.POST.dict()
        response = insert_to_supabase('users', data)
        return JsonResponse(response, safe=False)