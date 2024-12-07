import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Chat

# Configure the API key
genai.configure(api_key="AIzaSyD86n_KS-M9iua5afV9majXo0lOj5M7FDA")  # Replace with your actual Gemini API key


# Function to call Gemini API
def ask_gemini(message):
    try:
        # Initialize the model (replace with the appropriate model ID)
        model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with the model you want to use

        # Get the response by generating content with the message
        response = model.generate_content(message)

        # Return the response text
        return response.text.strip()  # Or adjust as necessary based on the Gemini API response

    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return "Sorry, there was an error processing your request."


@login_required
def chatbot(request):
    # Get all the user's previous chat messages from the database
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        print(f"Received message: {message}")  # Debugging log

        if message:
            # Get the response from Gemini
            response = ask_gemini(message)

            # Save the chat conversation to the database
            chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
            chat.save()

            # Return the message and response in JSON format for AJAX
            return JsonResponse({'message': message, 'response': response})
        else:
            print("No message received.")
            return JsonResponse({'error': 'Message is required'}, status=400)

    # If it's a GET request, return the chatbot page with all previous chats
    return render(request, 'chatbot/chatbot.html', {'chats': chats})
