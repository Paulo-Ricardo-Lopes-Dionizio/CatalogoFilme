import google.generativeai as genai

API_KEY = 'AIzaSyAikLCGg53JFwg83cS1euYuTPuw-ZTbaaI'

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

# Inicialização da sessão de bate-papo
history = []  # Histórico da conversa
chat = model.start_chat(history=history)

try:
    while True:

        question = input("Você: ")

        if question.strip() == '':
            break

        response = chat.send_message(question)
        history.append((question, response.text))  # Atualização do histórico

        # Exibição da resposta do modelo
        print('\n')
        print(f"Carlos_AI: {response.text}")
        print('\n')

# Finalização da sessão de bate-papo
finally:
    chat.end_chat()

print("Sessão de bate-papo encerrada.")
