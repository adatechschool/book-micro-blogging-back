"""
URL configuration for microblogging project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static
from users_app import views
 
urlpatterns = [
    path('', views.all_posts, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls'), name="login"),
    path('logout/', include('django.contrib.auth.urls'), name="logout"),
    path('admin/', admin.site.urls),
    path('users', views.all_posts, name='users'),
    path('profile/<int:id>/', views.user_profile, name='profile'),
    path('coucou-users/', views.fetch_users, name='fetch_users'),
    path('insert-user/', views.insert_user, name='insert_user'),
    #path('insert-post', views.insert_post, name="insert-post")
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) 
