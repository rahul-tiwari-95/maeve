from chatterbot.logic import LogicAdapter
from AdvancedNLP.textgeneration import solomonTextGeneration
from AdvancedNLP.zeroshot import solomonZeroShotClassification
from chatterbot.conversation import Statement
from SpeechNeuralNetworks.speechtext import solomonSpeech

class StoryModeLogicalAdapter(LogicAdapter):
    def __init__(self,chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    
    def can_process(self, statement):
        if statement.text.startswith('Activate cognitive mode'):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        maeve = solomonTextGeneration()
        solomon = solomonSpeech()
        #payload = input()
        payload=solomon.speech2text()
        response_statement = Statement(text=maeve.textGenerationNeuralNetwork(payload))
        #print(response_statement)
        solomon.text2speech(str(response_statement))
        return response_statement
        

class CustomerModeLogicalAdapter(LogicAdapter):
    def __init__(self,chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    
    def can_process(self,statement):
        if statement.text.startswith('Activate deep language analysis'):
            return True
        else:
            return False
        
    
    def process(self, input_statement, additional_response_selection_parameters):
        maeve = solomonZeroShotClassification()
        solomon = solomonSpeech()
        print("Speak the statement you want me to analyze. \n")
        inputs = solomon.speech2text()
        numberOfLabels=int(input("Nice, now tell me how many labels you want me to analyse for?"))
        array =[]
        while numberOfLabels >0:
            value = input("Type your label type: \n")
            array.append(value)
            numberOfLabels = numberOfLabels - 1

        parameters = array
        maeve.zeroShotClassification(inputs, array)
        response_statement = Statement( " \n " + "Deep Language Analysis Complete")
        return response_statement

