from django.shortcuts import render
from django.http import JsonResponse
from .llm import generate_response  # LLM 코드 import
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
            response = generate_response(user_input)
            return JsonResponse({'response': response})
        except json.JSONDecodeError: # 잘못된 JSON 데이터로 인한 서버 오류 방지
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)