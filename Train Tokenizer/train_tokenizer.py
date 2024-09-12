import sentencepiece as spm

# Train the SentencePiece model with a smaller vocabulary size
spm.SentencePieceTrainer.train(
    '--input=sinhala_corpus.txt --model_prefix=sinhala_tokenizer --vocab_size=4195 --model_type=bpe'
)
