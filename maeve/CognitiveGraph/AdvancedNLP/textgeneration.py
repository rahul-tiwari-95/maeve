import json
import requests
headers = {"Authorization": f"Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"

#Text Generation Neural Network Class by Hugging Transformers



class solomonTextGeneration:
    def __init__(self):
        print("Authentication Success")
        print("Activating Cognitive Neural Network by Solomon AI \n")

    
    def textGenerationNeuralNetwork(self, statement):
        payload = {"inputs": str(statement), "use_gpu": True, "max_length": 140}
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        text = json.loads(response.content.decode("utf-8"))
        return text[0].get('generated_text')









# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))



# data = query({"inputs": "breakups are nasty"})
# print(data)