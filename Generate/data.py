import openai

msg_history = []


def add_msg(role, theme):
    msg_history.append({'role': role, 'content': theme})


def generate(ask):
    add_msg('user', ask)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=msg_history
    )
    answer = response['choices'][0]['message']['content']
    add_msg('assistant', answer)
    return answer

