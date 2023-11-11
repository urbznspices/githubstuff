
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set the model to evaluation mode
model.eval()

# Define a function to generate text from the model


def generate_text(prompt, length=1000):
    # Encode the prompt
    encoded_prompt = tokenizer.encode(prompt, return_tensors='pt')

    # Create the attention mask
    attention_mask = torch.ones(encoded_prompt.shape, dtype=torch.long)

    # Generate text
    output = model.generate(
        input_ids=encoded_prompt,
        max_length=length,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id
        attention_mask=attention_mask,  # Pass the attention mask
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)


# Test the chatbot
while True:
    prompt = input('You: ')
    response = generate_text(prompt)
    print('Bot:', response)
    print("\n\n\n\n\n\n\n\n\n\n\n")
