import openai

def query_chat_gpt(query):
    openai.api_key = 'sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop'

    parameters = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, 
                     {'role': 'user', 'content': query}]
    }
    response = openai.ChatCompletion.create(**parameters)
    chat_reply = response.choices[0].message.content
    return chat_reply

# print(query_chat_gpt("What is API?"))


