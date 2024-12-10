import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Prefetch
from users_app import templates
from users_app.models import Post, User, Tag
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase

def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    } 
    print(f"🦄 {posts}")
   
    return render(request, 'first_template.html', context)

def fetch_posts_details(request):
    posts_details = Post.objects.select_related('user').prefetch_related('tags')
    posts_json = serializers.serialize("json", posts_details)

    context = {
        'posts_details': posts_details,
    }
    print(f"🦄 {posts_json}")
    return render(request, 'second_template.html', context)

# post_content_list : string list
# post_username_list : string list

# for i = 0
#   post_content_list[i] + post_username_list[i]
#
# post_list : (string * string) list
#              content * username

def merge (lst1, lst2):
    return [(lst1[i]["content"], lst2[i]["user_id"]) for i in range(0, len(lst1))]

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

def user_profile(request, id):
    queryUserPosts = Post.objects.filter(user_id=id)
    userPosts = serializers.serialize('json', queryUserPosts)
    
    queryUserInfo = User.objects.filter(id=id)
    userInfo = serializers.serialize('json', queryUserInfo)
    
    return JsonResponse(userInfo, safe=False)
