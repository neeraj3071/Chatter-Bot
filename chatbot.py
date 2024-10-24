from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

mybot = ChatBot(
name="PyBot", 
read_only=True,
logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.BestMatch"])

small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']

math_talk_1 = ['pythagorean theorem',
          'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
          'c*2 = a2 + b*2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk, math_talk_2):
 list_trainer.train(item)
 
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
 
print(my_bot.get_response("hi"))

print(my_bot.get_response("I feel awesome today"))

print(my_bot.get_response("What's your name"))

print(my_bot.get_response("show me the pythagorean theorm"))

print(my_bot.get_response("do you know law of cosines"))

while True:
 try:
  bot_input = input("You: ")
  bot_input = bot.get_response(bot_input)
  print(f"{my_bot.name}: {bot_response}")
 except (KeyboardInterrupt, EOFError, SystemExit):
  break;
