import json
import requests

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

context = "BDGDAO Marketplace is a product from Project-Bodega Syndicate C-Corp"

#Corpus Data for Project-Bodega business
text = " BDGDAO (bdgdao.com) is a product from Project-Bodega Syndicate C-Corp. Project-Bodega was founded in February of 2022 at New York. sudo88 or Rahul Tiwari is the creator and CEO at Project-Bodega. Rahul engineered the BDGDAO app / website and Solomon AI. Project-Bodega is based out of New York. Project-Bodega was created because sudo88 felt that young creators like him do not have the right tools needed to build a sustainable business. Current alternatives like Instagram or Shopify is expensive, have content restrictions, charge high commission on sales, do not allow instant payouts and provide zero data control.  Due to current cohort of companies, young creators can not launch or grow their product without significant capital investment which is primarily spent on performance marketing and digital services commissions out of which 60% goes to the big companies. Out of the 60%, 40% is spent paying commissions or website hosting fees and the rest 60% is spent on paid advertising. \n The problem statement, we're trying to solve is that young creators can't launch or grow their product without significant monetary and social investment, which is primarily spent on hosting fees, commissions and inefficient paid ADs \n.Why is project bodega necessary?, because in 2022, anyone with the right product should be able to harness the power of internet. But the reality is different, big companies like facebook, google and shopify have monopolized the market and because of their outdated rules, young creators have to suffer. \nsOur solution to this problem is giving the platform for free where the creators can setup their shop and do all kinds of transactions for free. If creators want to grow their business further, we will charge for targeted distribution. We will monetize the data and allow our members to leverage that data to reach more customers or creators. "

class solomonRobertaNeuralNetwork:
    def __init__(self):
        print("Authentication Success")
        print("Activating Zero Shot Classification by Solomon AI \n")

    def robertaNeuralNetwork(self, input_statement):
        payload = {"inputs": {
            "question": str(input_statement),
            "context": text
        }}
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))