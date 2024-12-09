import requests
import json
from django.http import JsonResponse
from django.conf import settings

SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_KEY

headers = {
"apikey": SUPABASE_KEY,
"Content-Type": "application/json",
"Authorization": f"Bearer {SUPABASE_KEY}"
}

def fetch_from_supabase(endpoint):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.get(url, headers=headers)
    return response.json()

def insert_to_supabase(endpoint, data):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print(f"Success: {response.status_code} - {response.text}")
            return True
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return False
    except:
        return False