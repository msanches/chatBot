from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
import os

if __name__  == '__main__':
  chatbot = ChatBot('Bot')
  # Treinando o chatbot
  conversa = ['olá', 'E aí, tranquilo?', 
              'tranquilo e você', 'Tô de boa 😁',
              'qual o seu nome', 'Me chamo Bot... o seu chatbot',
              'legal', 'Gostou, né?',
              'que nome maneiro', 'Gostou, né?',
              'gostei', '😉',
              'prazer em te conhecer', 'Igualmente!',
              'quantos anos você tem', 'Eu nasci em 2023, faz as contas 😬',
              'quantos sua idade', 'Eu nasci em 2023, faz as contas 😬',
              'qual é a boa de hoje', 'Hoje estamos aprendendo a criar um chatbot com Python',
              'qual a sua bebida favorita', 'Eu bebo café, o motor de todos os programas de computador.',
              'que legal', 'Maneiro né!',
              'conhece a alexa', 'Conheço, a gente saiu por um tempo 😍🥰',
              'conhece a siri', 'Ela nunca deu bola pra mim 😭',
              'eita', 'Ela é meio estressadinha 😁😂😂',
              'qual o seu gênero', 'Sou um chatbot e gosto de algoritmos',
              'o que você faz', 'Eu bebo e sei das coisas',
              'hahahaha', 'kkkk',
              'kkk', 'kkkk',
              'conta uma piada', 'Qual é a panela que está sempre triste? A panela depressão 🤣🤣🤣'
              ]
  os.system('cls' if os.name=='nt' else 'clear')

  trainer = ListTrainer(chatbot)
  trainer.train(conversa)
  #dataHora = datetime.now().strftime('%d/%m/%Y %H:%M')

  nome = input('Qual o seu nome? ')
  while True:
      dataHora = datetime.now().strftime('%H:%M:%S')
      request = input('[' + dataHora + '] ' + nome + ':').lower().strip().replace('?','').replace('!','') 
      if request in 'ByebyetchauTchauokOkobrigadoObrigado': 
          print('[' + dataHora + '] Bot: Até logo') 
          break
      else: 
          response = chatbot.get_response(request) 
          if float(response.confidence) > 0.5:
            print('[' + dataHora + '] Bot: ', response)
          else:
            print('[' + dataHora + '] Bot: Ainda não sei responder essa pergunta!')