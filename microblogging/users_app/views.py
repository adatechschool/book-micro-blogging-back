from django.shortcuts import render
from django.http import JsonResponse
from users_app import templates
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase
# from users_app.models import User
from users_app.models import Post

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

def fetch_users(request):
    data = fetch_from_supabase('users_app_user')
    return JsonResponse(data, safe=False)

def insert_user(request):
    if request.method == 'POST':
        data = request.POST.dict()
        response = insert_to_supabase('users_app_user', data)
        return JsonResponse(response, safe=False)