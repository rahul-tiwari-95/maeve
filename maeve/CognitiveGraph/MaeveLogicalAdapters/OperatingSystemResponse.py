from chatterbot.logic import LogicAdapter
from AdvancedNLP.textgeneration import solomonTextGeneration
from chatterbot.conversation import Statement
from SpeechNeuralNetworks.speechtext import solomonSpeech

class StoryModeLogicalAdapter(LogicAdapter):
    def __init__(self,chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    
    def can_process(self, statement):
        if statement.text.startswith('Cognitive mode'):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        maeve = solomonTextGeneration()
        bernard = solomonSpeech()
        #payload = input()
        payload=bernard.speech2text()
        response_statement = Statement(text=maeve.textGenerationNeuralNetwork(payload))
        #print(response_statement)
        #bernard.text2speech(str(response_statement))
        return response_statement
        

