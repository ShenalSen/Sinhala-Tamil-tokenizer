# Sinhala Tokenizer using SentencePiece

This repository contains the implementation of a **Sinhala Tokenizer** built using **SentencePiece**. The tokenizer was trained on a corpus of Sinhala text and can be used to tokenize Sinhala sentences for NLP tasks such as text processing and building language models.

## Project Overview

- **Language**: Sinhala
- **Model**: Byte-Pair Encoding (BPE)
- **Vocabulary Size**: 4195 tokens
- **Training Tool**: [SentencePiece](https://github.com/google/sentencepiece)
- **Script**: Implemented in Python via a Jupyter Notebook (`.ipynb`)

## Files in This Repository

- **`train_tokenizer.ipynb`**: Jupyter notebook used to train the Sinhala tokenizer using SentencePiece.
- **`sinhala_tokenizer.model`**: The trained tokenizer model file.
- **`sinhala_tokenizer.vocab`**: The vocabulary file corresponding to the tokenizer.
- **`sinhala_corpus.txt`**: The corpus used to train the tokenizer.
- **`train_tokenizer.py`**: Python script version of the Jupyter notebook for training the tokenizer from scratch.

## Getting Started

### Requirements

To run this project, you'll need the following dependencies:

- Python 3.6+
- SentencePiece
- Jupyter Notebook (if running `.ipynb` file)
  
You can install the required Python packages using `pip`:

```bash
pip install sentencepiece
```

### Training the Tokenizer

To train the tokenizer, you can either use the Jupyter notebook or run the Python script. 

#### Using Jupyter Notebook:

1. Open `train_tokenizer.ipynb` in Jupyter.
2. Run the cells step by step to train the tokenizer using the provided corpus (`sinhala_corpus.txt`).

#### Using Python Script:

Alternatively, you can run the `train_tokenizer.py` script directly from the command line:

```bash
python train_tokenizer.py
```

This will generate the tokenizer files: `sinhala_tokenizer.model` and `sinhala_tokenizer.vocab`.

### Tokenizing Sinhala Text

Once the tokenizer is trained, you can use it to tokenize Sinhala text. Here is a basic example:

```python
import sentencepiece as spm

# Load the trained tokenizer
sp = spm.SentencePieceProcessor(model_file='sinhala_tokenizer.model')

# Tokenize a Sinhala sentence
sinhala_sentence = "සංජුල ඔබට කෙසේද?"
tokens = sp.encode(sinhala_sentence, out_type=str)
print(tokens)
```

### Repository Structure

```
.
├── sinhala_corpus.txt          # Corpus used for training
├── sinhala_tokenizer.model     # Trained tokenizer model
├── sinhala_tokenizer.vocab     # Tokenizer vocabulary
├── train_tokenizer.ipynb       # Jupyter notebook for training
├── train_tokenizer.py          # Python script for training
└── README.md                   # Project documentation
```

## How to Contribute

Feel free to fork this repository, open an issue, or submit a pull request if you'd like to contribute improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
