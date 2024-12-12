import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase
from users_app import templates
from users_app.models import Post, Tag, Follower, AuthUser
from django.contrib.auth.models import User
from datetime import datetime


@login_required
def all_posts(request):
    posts = Post.objects.select_related('user').all().order_by('-created_at')
    print(f"🦀 {posts}")
    
    
    list_posts = []
    
    for post in posts:
        p = model_to_dict(post)
        print(f"🪲 {p}")
        print(f"{post.created_at}")
        p["tags"] = []
        p["user"] = model_to_dict(post.user)["username"]
        p["user_id"] = model_to_dict(post.user)["id"]
        p["post_id"] = model_to_dict(post)["id"]
        publish_date = post.created_at
        publish_date_str = publish_date.strftime("%Y-%m-%d %H:%M:%S")
        print(f"🐣 {publish_date_str}")
        print(type(publish_date_str))
        p["created_at"] = publish_date_str
        for tag in post.tags.all():
            p["tags"].append(tag.tag)
        list_posts.append(p)
    print(f"🪼 {list_posts}")        
    context = {
        'posts': json.dumps(list_posts),
    }
    j = json.dumps(list_posts)
    print(f"🦄 {j}")
   
    return render(request, 'home.html', context)


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
    query_user_posts = Post.objects.filter(user_id=id)
    
    #on transforme le queryset en liste de dictionnaires
    posts_list = list(query_user_posts.values('id', 'user_id', 'content', 'tags','parent_id'))
    print(f"🐹 {posts_list}")
    
    # for post in posts_list:
    #     created_date = post["created_at"]
    #     created_date_str = created_date.strftime("%Y-%m-%d %H:%M:%S")
    #     post["created_at"] = created_date_str
    
    
    query_user_info = AuthUser.objects.get(id=id)
    user_info = model_to_dict(query_user_info)
    print(f"🐻 {user_info} ")
    # print(f"🟢 {query_user_info.bio}")
    
    #on créée un dictionnaire User avec les info voulues
    user_info =  {
        'id': query_user_info.id,
        'username': query_user_info.username,
        'bio': query_user_info.bio,
    }
    
    print(f"🧘‍♂️ {user_info}")

    
    query_following = Follower.objects.filter(follower_id=id)
    following_list = list(query_following.values('followed_id', 'follower_id'))
    
    
    #on merge les info des posts et les infos du user dans un dictionnaire:
    response_data = {
        'user': json.dumps(user_info),
        'posts': json.dumps(posts_list),
        'following': json.dumps(following_list)
    }
    
    context = { 
        'data': json.dumps(response_data)
    }

    print(f"🍋 {response_data}")

    data_json = json.dumps(response_data)
    print(f"🐼 {data_json}")
    
    return render(request, 'profile.html', context)


# @csrf_exempt
# def insert_post(request):




 
        