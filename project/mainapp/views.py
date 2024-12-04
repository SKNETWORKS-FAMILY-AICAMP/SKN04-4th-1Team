from django.shortcuts import render
from django.http import JsonResponse
from .llm import generate_response  # LLM 코드 import

def home(request):
    return render(request, 'mainapp/home.html')

def chat(request):
    return render(request, 'mainapp/chat.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        response = generate_response(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)