import openai

msg_history = []
is_end = [False]


def create_theme(theme):
    msg_history.append({'role': 'system', 'content': theme})


def generate():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=msg_history
        )
        return response['choices'][0]['message']['content']
    except BaseException:
        is_end[0] = True


