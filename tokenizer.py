import re

def simple_tokenizer(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words
    tokens = text.split()
    
    return tokens


# Example usage
sentence = "Hello Hansika! Welcome to AI learning."
tokens = simple_tokenizer(sentence)

print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)