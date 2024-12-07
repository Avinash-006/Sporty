from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render



from django.shortcuts import render
from .utils import send_prompt_and_receive_reply

def chatbot_index(request):
    reply = ""
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        try:
            reply = send_prompt_and_receive_reply(prompt)
        except Exception as e:
            reply = str(e)

    return render(request, 'chatbotapp/index.html')
