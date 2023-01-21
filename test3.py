# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

#Sentiment Analysis
model_inputs = {
    'max_new_tokens': 2,
    'prompt': 
'''Label the tweets as either "positive", "negative", "mixed", or "neutral":

Tweet: I can say that there isn't anything I would change.
Label: positive

Tweet: I'm not sure about this.
Label: neutral

Tweet: I liked some parts but I didn't like other parts.
Label: mixed

Tweet: I think the background image could have been better.
Label: negative

Tweet: I really like it.
Label:'''}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())