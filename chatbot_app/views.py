from django.shortcuts import render
from django.http import JsonResponse
import xgoogle.generativeai as genai
from django.conf import settings
import json

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

def chatbot_view(request):
    if request.method == 'POST':
        try:
            raw_body = request.body.decode('utf-8')  # Decode raw request
            print("Received Data:", raw_body)  # Debugging

            data = json.loads(raw_body)
            user_message = data.get('message', '').strip()  # Fix: Correct key

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            bot_response = generate_ai_response(user_message)
            return JsonResponse({'bot_response': bot_response})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return render(request, 'chatbot_app/chatbot.html')

def generate_ai_response(user_message):
    try:
        model = genai.GenerativeModel("models/gemini-1.0-pro")  # ✅ Corrected model name
        response = model.generate_content(user_message)
        
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "I'm sorry, I couldn't generate a response."
    
    except Exception as e:
        print("Error:", str(e))  # Debugging
        return "An error occurred while generating a response."
