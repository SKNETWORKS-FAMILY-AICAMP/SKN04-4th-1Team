import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from model import book_model
from django.shortcuts import render
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'mainapp/home.html')

def chat(request):
    return render(request, 'mainapp/chat.html')

def get_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '')
            response = book_model.get_response(user_input)
            return JsonResponse({'response': response})
        except json.JSONDecodeError: # 잘못된 JSON 데이터로 인한 서버 오류 방지
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)