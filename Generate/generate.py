import json
import aiohttp
from config import api_key

msg_history = dict([])


def add_msg(id, role, theme):
    if id in msg_history:
        msg_history[id].append({'role': role, 'content': theme})
    else:
        msg_history[id] = []
        msg_history[id].append({'role': role, 'content': theme})


async def generate(id, ask):
    add_msg(id, 'user', ask)
    response = await send_request(id)
    answer = json.loads(response)['choices'][0]['message']['content']
    add_msg(id, 'assistant', answer)
    return answer


async def send_request(id):
    async with aiohttp.ClientSession() as session:
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {
            "model": "gpt-3.5-turbo-0301",
            "messages": msg_history[id]
        }
        async with session.post(api_url, headers=headers, json=data) as response:
            if response.status == 402:
                raise ChildProcessError()
            if response.status == 400:
                raise SystemError
            return await response.text()
