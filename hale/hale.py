from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from SpeechNeuralNetworks.speechtext import solomonSpeech


chatbot = ChatBot("Hale",
logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch"
    }
]
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "KnowledgeGraph/OriginStory/introduction.yml"

)

print(" ============ BDGDAO Shareholder Authentication Successs =================")
print("Hello shareholder, I am Hale. I am responsible for investor relations at BDGDAO.")
print("Type something to begin......")


#hale = solomonSpeech()
while True:
    try:
        user_input = input("Human >")
        #user_input = hale.speech2text()
        print("============ ACCESSING SOLOMON NEURAL NETWORKS ================= \n")
        bot_response = chatbot.get_response(user_input)
        print("Charlotte Hale @ BDGDAO >", bot_response)
        #hale.text2speech(str(bot_response))

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
