# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

#Text summarization
model_inputs = {
    'max_new_tokens': 5,
    'prompt': 
'''Given a review from Amazon's food products, the task is to generate a short summary of the given review in the input.
Input: I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than most.
Output: Good Quality Dog Food

Input: Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as 'Jumbo'.
Output: Not as Advertised

Input: My toddler loves this game to a point where he asks for it. That's a big thing for me. Secondly, no glitching unlike one of their competitors (PlayShifu). Any tech I don’t have to reach out to support for help is a good tech for me. I even enjoy some of the games and activities in this. Overall, this is a product that shows that the developers took their time and made sure people would not be asking for refund. I’ve become bias regarding this product and honestly I look forward to buying more of this company’s stuff. Please keep up the great work.
Output:'''}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())