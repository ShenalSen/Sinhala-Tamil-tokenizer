from transformers import AutoTokenizer, AutoModel

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("path/to/sinhala_tokenizer.model")

# Tokenize input text
sinhala_sentence = "ඔබට කෙසේද? මම කාර්යබහුලය්."
tokens = tokenizer(sinhala_sentence)
print("Token IDs:", tokens['input_ids'])

# Load a pretrained LLM (for example, a BERT model)
model = AutoModel.from_pretrained("path/to/pretrained_sinhala_model")

# Pass the token IDs into the LLM
outputs = model(**tokens)
print(outputs)
