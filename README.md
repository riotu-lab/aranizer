# AraNizer

## Description
`AraNizer` is a sophisticated toolkit of custom tokenizers tailored for Arabic language processing. Integrating advanced methodologies such as SentencePiece and Byte Pair Encoding (BPE), these tokenizers are specifically designed for seamless integration with the `transformers` and `sentence_transformers` libraries. The `AraNizer` suite offers a range of tokenizers, each optimized for distinct NLP tasks and accommodating varying vocabulary sizes to cater to a multitude of linguistic applications.

## Key Features
- **Versatile Tokenization:** Supports multiple tokenization strategies (BPE, SentencePiece) for varied NLP tasks.
- **Broad Vocabulary Range:** Customizable tokenizers with vocabulary sizes ranging from 32k to 86k.
- **Seamless Integration:** Compatible with popular libraries like transformers and sentence_transformers.
- **Optimized for Arabic:** Specifically engineered for the intricacies of the Arabic language.

## Installation
Install AraNizer effortlessly with pip:
```bash
pip install aranizer
```

## Usage
### Importing Tokenizers
Import your desired tokenizer from AraNizer. Available tokenizers include:
- BEP variants: aranizer_bpe50k, aranizer_bpe64k,
- SentencePiece variants: aranizer_bpe86k, aranizer_sp32k, aranizer_sp50k, aranizer_sp64k, aranizer_sp86k.

```python
from aranizer import aranizer_sp32k  # Replace with your chosen tokenizer

#Load your tokenizer:
tokenizer = aranizer_sp32k.get_tokenizer()
```

### Tokenizing Text
Tokenize Arabic text using the selected tokenizer:

```python
text = "مثال على النص العربي"  # Example Arabic text
tokens = tokenizer.tokenize(text)
print(tokens)
```

### Encoding and Decoding

Encode text into token ids and decode back to text. 

**Encoding:** To encode text, use the encode method. 
```python
text = "مثال على النص العربي"  # Example Arabic text
encoded_output = tokenizer.encode(text, add_special_tokens=True)
print(encoded_output)
```

**Decoding:** To convert token ids back to text, use the decode method:
```python
decoded_text = tokenizer.decode(encoded_output)
print(decoded_text)
```

## Available Tokenizers

```bash
- aranizer_bpe32k: Based on BEP Tokenizer with Vocab Size of 32k
- aranizer_bpe50k: Based on BEP Tokenizer with Vocab Size of 50k
- aranizer_bpe64k: Based on BEP Tokenizer with Vocab Size of 64k
- aranizer_bpe86k: Based on BEP Tokenizer with Vocab Size of 86k
- aranizer_sp32k: Based on Sentence Peice Tokenizer with Vocab Size of 32k
- aranizer_sp50k: Based on Sentence Peice Tokenizer with Vocab Size of 50k
- aranizer_sp64k: Based on Sentence Peice Tokenizer with Vocab Size of 64k
- aranizer_sp86k: Based on Sentence Peice Tokenizer with Vocab Size of 86k
```

## System Requirements
- Python 3.x
- transformers library
  
## Contact:
For queries or assistance, please contact riotu@psu.edu.sa.

## Acknowledgments:
This work is maintained by the Robotics and Internet-of-Things Lab at Prince Sultan University. 

## Team:
- Prof. Anis Koubaa (Lab Leader)
- Dr. Lahouari Ghouti (NLP Team Leader)
- Eng. Omar Najjar (AI Research Assistant)
- Eng. Serry Sebai (NLP Research Engineer)

## Version:
0.1.8

## Citations:
Coming soon


