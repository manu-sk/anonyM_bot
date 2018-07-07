


'''This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.


chatbot = ChatBot(
    'Export Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# First, lets train our bot with some data
chatbot.train('chatterbot.corpus.english')

# Now we can export the data to a file
chatbot.trainer.export_for_training('./my_export.json')

response = chatbot.get_response('I would like to book a flight.')

print(response)'''
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "anonyM_bot",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
  #  input_adapter="chatterbot.input.TerminalAdapter",
    logic_adapters=[
        { "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response",
          },
            "chatterbot.logic.MathematicalEvaluation"
    ],


)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('./my_export.json')
# Print an example of getting one math based response

while True:
    try:
        query = input()
        response = bot.get_response(query)
        print(response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break