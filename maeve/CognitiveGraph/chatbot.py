from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from SpeechNeuralNetworks.speechtext import solomonSpeech

chatbot = ChatBot("Maeve",
logic_adapters=[
    {
        #"import_path": "chatterbot.logic.BestMatch",
        "import_path": "MaeveLogicalAdapters.OperatingSystemResponse.StoryModeLogicalAdapter",
        #'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.70
     },
    {
        "import_path": "chatterbot.logic.BestMatch"
    }
])
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "../KnowledgeGraph/OriginStory/corpus/introduction.yml",
    "../KnowledgeGraph/OriginStory/corpus/emotionalaffect.yml",
    "../KnowledgeGraph/OriginStory/corpus/psychology.yml",
    "../KnowledgeGraph/OriginStory/corpus/maeve.yml",
    "../KnowledgeGraph/OriginStory/corpus/BDG-faq.yml"
)

print("My name is Maeve. I am the Chief Experience Officer at BDGDAO.")
print("I have been described as rude/savage but I am improving as I meet more lovely humans like you.")
print("Welcome to $BDGDAO")
print('Type something to begin...')

# The following loop will execute each time the user enters input
maeve = solomonSpeech()
while True:
    try:

        user_input =  input("Human >")
        #user_input = maeve.speech2text()
        print("============ RUNNING SOLOMON NEURAL NETWORKS ================= \n")
        bot_response = chatbot.get_response(user_input)
        print("*** Generating Linguistic Response *** \n")

        print("Maeve @ BDGDAO >" ,bot_response)
        #maeve.text2speech(str(bot_response))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break