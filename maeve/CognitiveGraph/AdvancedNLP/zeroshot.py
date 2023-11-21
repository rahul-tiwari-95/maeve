import json
import requests


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

#Zero Shot Class Classification 

class solomonZeroShotClassification:
    def __init__(self):
        print("Authentication Success")
        print("Activating Zero Shot Classification by Solomon AI \n")

    
    def zeroShotClassification(self, inputs, parameters):

        payload = {"inputs": str(inputs), "parameters": {"candidate_labels": (parameters)}}
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        generatedResponse = json.loads(response.content.decode("utf-8"))
        scores = [] #initializing empty list
        labels = []
        i=1
        for score in generatedResponse.get('scores'):
            scores.append(score*100)
        for label in generatedResponse.get('labels'):
            labels.append(label)
        while i > 0:
            print("======== Sentiment Analysis Complete ======== \n")
            for score in scores:
                print("Probablity %", score, "\n" )
            for label in labels:
                print("Labels: ", label, "\n")
            i  = i-1
        
        
        
                


