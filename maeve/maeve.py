from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from SpeechNeuralNetworks.speechtext import solomonSpeech
from CognitiveGraph.SpeechNeuralNetworks.speechtext import solomonSpeech

chatbot = ChatBot("Maeve3.0",
logic_adapters=[
    # {
    #     "import_path": "CognitiveGraph.MaeveLogicalAdapters.OperatingSystemResponse.StoryModeLogicalAdapter",
    #     'maximum_similarity_threshold': 0.90
    #  },
    #  {
    #     "import_path": "CognitiveGraph.MaeveLogicalAdapters.OperatingSystemResponse.CustomerModeLogicalAdapter",
    #     'maximum_similarity_threshold': 0.90
    #  },
     {
         "import_path" : "chatterbot.logic.BestMatch",
         
     }
    # {
    #     "import_path": "MaeveLogicalAdapters.ConversationalLogicalAdapter.BestMatch",


    # }
])
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "KnowledgeGraph/OriginStory/corpus/introduction.yml",
    "KnowledgeGraph/OriginStory/corpus/emotionalaffect.yml",
    "KnowledgeGraph/OriginStory/corpus/psychology.yml",
    "KnowledgeGraph/OriginStory/corpus/maeve.yml",
    "KnowledgeGraph/OriginStory/corpus/BDG-faq.yml"
)

print("My name is Maeve. I am the Guest Experience Officer at BDGDAO.")
print(" I am still in Beta mode and the responses I am generating are dynamic. So, expect slow response time for now.")
print("Welcome to $BDGDAO")
print('Type something to begin...')

# The following loop will execute each time the user enters input
maeve = solomonSpeech()
while True:
    try:
        
        #user_input =  input("Human >")
        user_input = maeve.speech2text()
        print("============ ACCESSING SOLOMON NEURAL NETWORKS ================= \n")
        print("*** Generating Linguistic Response *** \n")
        bot_response = chatbot.get_response(user_input) 
        print("Maeve v2.882 @ BDGDAO >" ,bot_response)
        maeve.text2speech(str(bot_response))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


# import os    
# import time    
# second = 0    
# minute = 0    
# hours = 0    
# while(True):    
#     print("Running Simulations")    
#     print('\n\n\n\n\n\n\n')    
#     print('\t\t\t\t-------------')    
#     print('\t\t\t\t  %d : %d '%(minute,second))    
#     print('\t\t\t\t-------------')    
#     time.sleep(1)    
#     second+=1    
#     if(second == 60):    
#         second = 0    
#         minute+=1    
#     if(minute == 60):    
#         minute = 0    
#         hours+=1;    
#     os.system('cls')    