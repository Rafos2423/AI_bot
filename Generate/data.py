import openai

msg_history = []


def add_msg(role, theme):
    msg_history.append({'role': role, 'content': theme})


def generate():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=msg_history
    )
    return response['choices'][0]['message']['content']

