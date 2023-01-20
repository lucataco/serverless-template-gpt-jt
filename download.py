# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface GPTJ model

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    print("downloading model...")
    tokenizer = AutoTokenizer.from_pretrained("togethercomputer/GPT-JT-6B-v1")
    print("done")

    print("downloading tokenizer...")
    model = AutoModelForCausalLM.from_pretrained("togethercomputer/GPT-JT-6B-v1")
    print("done")

if __name__ == "__main__":
    download_model()