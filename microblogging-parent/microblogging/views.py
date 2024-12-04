from django.http import JsonResponse
from .supabase_utils import fetch_from_supabase, insert_to_supabase

def fetch_data_view(request):
    data = fetch_from_supabase('users')
    return JsonResponse(data, safe=False)

def insert_data_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        response = insert_to_supabase('users', data)
        return JsonResponse(response, safe=False)