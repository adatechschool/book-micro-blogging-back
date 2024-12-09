from django.shortcuts import render
from django.http import JsonResponse
from users_app import templates
from django.views.decorators.csrf import csrf_exempt
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase
import json
from users_app.models import Post, User, Tag

# def index(request):
#     users = User.objects.all().values()
#     context = {
#         'users': users,
#     } 
#     print(f"🦄 {users}")
#     return render(request, 'first_template.html', context)

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    } 
    print(f"🦄 {posts}")
    return render(request, 'first_template.html', context)

def users(request):
    users = User.objects.first()
    posts = Post.objects.first()
    context = {
        'users': [{"username":users.username}]
    } 
    return render(request, 'index.html', context)


def fetch_users(request):
    data = fetch_from_supabase('users_app_user')
    return JsonResponse(data, safe=False)

@csrf_exempt
def insert_user(request):
    if request.method == 'POST':
        # data = request.POST.dict()
        data = json.loads(request.body)
        print(f"🐯 {data}")
        response = insert_to_supabase('users_app_user', data)
        if response == True:
            return JsonResponse({
                "result": "✅ L'utilisateur a bien été créé."
            }, status=201)
        else:
            return JsonResponse({
                "result": "⛔️ L'utilisateur (email et/ou username) existe déjà."
            }, status=403)
