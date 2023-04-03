import openai
from engine import print_log
import time

msg_history = []


def create_theme(theme):
    msg_history.append({'role': 'system', 'content': theme})


def start_generate(ask):
    msg_history.append({'role': 'user', 'content': ask})
    print_log('txt', ask)
    start = time.time()
    answer = generate()
    duration = round(time.time() - start, 2)
    print_log(f'scs - {duration}s', answer)
    msg_history.append({'role': 'assistant', 'content': answer})
    return answer


def generate():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg_history
    )
    return response['choices'][0]['message']['content']
