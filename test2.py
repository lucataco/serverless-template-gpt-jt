# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

#Question Answering
model_inputs = {
    'max_new_tokens': 3,
    'prompt': 
'''Please answer the following question:

Question: What is the capital of Canada?
Answer: Ottawa

Question: What is the currency of Switzerland?
Answer: Swiss franc

Question: In which country is Wisconsin located?
Answer:'''}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())