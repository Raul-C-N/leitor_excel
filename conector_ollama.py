import ollama

from ollama import Client

# Replace with your local network IP if localhost does not work
client = Client(host='http://localhost:11434')

def perguntar_ia(pergunta):
    try:
        response = client.chat(
            model='gemma4:e4b',
            messages=[{'role': 'user', 'content': pergunta}]
        )
        # print(response['message']['content'])
        return(response['message']['content'])
    except Exception as e:
        print(f"\n❌ Ocorreu um erro durante a chamada à API do Ollama: {e}")


