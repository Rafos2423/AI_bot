import json
import aiohttp
from config import api_key

msg_history = []


def add_msg(role, theme):
    msg_history.append({'role': role, 'content': theme})


async def generate(ask):
    add_msg('user', ask)
    response = await send_request()
    answer = json.loads(response)['choices'][0]['message']['content']
    add_msg('assistant', answer)
    return answer


async def send_request():
    async with aiohttp.ClientSession() as session:
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {
            "model": "gpt-3.5-turbo-0301",
            "messages": msg_history
        }
        async with session.post(api_url, headers=headers, json=data) as response:
            if response.status == 402:
                raise ChildProcessError()
            if response.status == 400:
                raise SystemError
            return await response.text()
