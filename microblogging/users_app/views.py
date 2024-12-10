from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
from users_app import templates
from django.views.decorators.csrf import csrf_exempt
from microblogging_project.supabase_utils import fetch_from_supabase, insert_to_supabase
import json
from users_app.models import Post, User, Tag, Follower
from users_app.forms import UploadPost


def all_posts(request):
    posts = Post.objects.all()
    list_posts = []
    
    for post in posts:
        p = model_to_dict(post)
        p["tags"] = []
        for tag in post.tags.all():
            p["tags"].append(tag.tag)
        list_posts.append(p)
    print(f"🪼 {list_posts}")        
    context = {
        'posts': list_posts,
    }
    j = json.dumps(list_posts)
    print(f"🦄 {j}")
   
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
    query_user_posts = Post.objects.filter(user_id=id)
    
    #on transforme le queryset en liste de dictionnaires
    posts_list = list(query_user_posts.values('id', 'user_id', 'content', 'parent_id', 'created_at'))
    print(f"🐹 {posts_list}")
    
    query_user_info = User.objects.get(id=id)
    print(f"🐻 {query_user_info} ")
    
    #on créée un dictionnaire User avec les info voulues
    user_info =  {
        'id': query_user_info.id,
        'username': query_user_info.username,
        'bio': query_user_info.bio
    }
    
    print(f"🧘‍♂️ {user_info}")
    print(type(user_info))
    
    query_following = Follower.objects.filter(follower_id=id)
    
    following_list = list(query_following.values('followed_id', 'follower_id'))
    print(f"🍓 {following_list}")
    
    #on merge les info des posts et les infos du user dans un dictionnaire:
    response_data = {
        'user': user_info,
        'posts': posts_list,
        'following': following_list
    }
    
    print(f"🍋 {response_data}")
    print(type(response_data))
    
    return JsonResponse(response_data, safe=True)

#EN CONSTRUCTION, PAS FONCTIONNEL
# @csrf_exempt
# def insert_post(request):
#     form = UploadPost(request.POST, request.FILES)
#     print(request.FILES)
#     return render(request, 'form_template.html', {'form': form})



 
        