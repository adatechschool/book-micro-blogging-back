import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from users_app import templates
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase
from users_app.models import Post, User, Tag

# def index(request):
#     users = User.objects.all().values()
#     context = {
#         'users': users,
#     } 
#     print(f"🦄 {users}")
#     return render(request, 'first_template.html', context)

@login_required
def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    } 
    print(f"🦄 {posts}")
   
    return render(request, 'first_template.html', context)
# post_content_list : string list
# post_username_list : string list

# for i = 0
#   post_content_list[i] + post_username_list[i]
#
# post_list : (string * string) list
#              content * username

def merge (lst1, lst2):
    return [(lst1[i]["content"], lst2[i]["user_id"]) for i in range(0, len(lst1))]

@login_required
def users(request):
    users = User.objects.all().values('username')
    users_list = list(users)
    
    posts_content = Post.objects.all().values('content')
    posts_content_list = list(posts_content)
    
    posts_username = Post.objects.all().values('user_id')
    posts_username_list = list(posts_username)
    
    posts_content_username = merge(posts_content_list, posts_username_list)
    
    context = {
        'users': json.dumps(users_list),
        'posts_content_username': json.dumps(posts_content_username),
    } 
    return render(request, 'index.html', context)

@login_required
def fetch_users(request):
    data = fetch_from_supabase('users_app_user')
    return render(request, "users.html")
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

@login_required
def user_profile(request, id):
    queryUserPosts = Post.objects.filter(user_id=id)
    userPosts = serializers.serialize('json', queryUserPosts)
    
    queryUserInfo = User.objects.filter(id=id)
    userInfo = serializers.serialize('json', queryUserInfo)
    
    return JsonResponse(userInfo, safe=False)
