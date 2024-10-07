import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load pre-trained model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()


def generate_review(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Create attention mask: 1 for actual tokens, 0 for padding tokens
    # The pad_token_id might not be available for GPT-2; set attention mask accordingly
    attention_mask = torch.ones(inputs.shape, dtype=torch.long)  # Default to 1s for GPT-2

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            attention_mask=attention_mask,
            pad_token_id=tokenizer.eos_token_id
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Generate synthetic reviews
synthetic_reviews = []
for _ in range(10):  # Generate 10 reviews
    prompt = "Write a review for a supplement."
    review = generate_review(prompt)
    synthetic_reviews.append(review)

# Save to CSV
df = pd.DataFrame(synthetic_reviews, columns=["review"])
df.to_csv('synthetic_reviews.csv', index=False)
print("Generated synthetic reviews saved to synthetic_reviews.csv")
