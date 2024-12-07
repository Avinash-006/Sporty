import requests



GEMINI_API_KEY = 'AIzaSyBnPexwrHzfZ70TlVVQmdSyL6eNXUSeTR0'


def send_prompt_and_receive_reply(prompt):
    url = "https://api.gemini.com/v1/send-prompt"
    headers = {
        'Content-Type': 'application/json',
        'X-GEMINI-APIKEY': GEMINI_API_KEY,  # Hard-coded API key
    }
    payload = {
        "prompt": prompt,
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get('reply', 'No reply found.')
    except requests.RequestException as e:
        raise Exception(f"Network error: {str(e)}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
