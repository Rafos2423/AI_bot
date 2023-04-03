import openai

msg_history = []


def create_theme(theme):
    msg_history.append({'role': 'system', 'content': theme})


def generate():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg_history
    )
    return response['choices'][0]['message']['content']
