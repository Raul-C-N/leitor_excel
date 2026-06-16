import ollama

from ollama import Client

# Replace with your local network IP if localhost does not work
# client = Client(host='http://localhost:11434')

# response = client.chat(
#     model='gemma4:latest',
#     messages=[{'role': 'user', 'content': 'Qual a capital do Brasil?'}]
# )

# print(response['message']['content'])



def perguntar_ia(pergunta):
    try:
        response = client.chat(
            model='gemma4:latest',
            messages=[{'role': 'user', 'content': pergunta}]
        )
        print(response['message']['content'])
        return(response['message']['content'])
    except Exception as e:
        print(f"\n❌ Ocorreu um erro durante a chamada à API do Ollama: {e}")
