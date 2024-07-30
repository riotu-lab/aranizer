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
BEP variants: get_bpe with keys bpe32, bpe50, bpe64, bpe86, bpe32T, bpe50T, bpe64T, bpe86T
SentencePiece variants: get_sp with keys sp32, sp50, sp64, sp86, sp32T, sp50T, sp64T, sp86T

```python
from aranizer import get_bpe, get_sp  # Import functions to retrieve tokenizers

# Example for importing a BPE tokenizer
bpe_tokenizer = get_bpe("bpe32")  # Replace with your chosen tokenizer key

# Example for importing a SentencePiece tokenizer
sp_tokenizer = get_sp("sp32")  # Replace with your chosen tokenizer key
```

### Tokenizing Text
Tokenize Arabic text using the selected tokenizer:

```python
text = "مثال على النص العربي"  # Example Arabic text

# Using BPE tokenizer
bpe_tokens = bpe_tokenizer.tokenize(text)
print(bpe_tokens)

# Using SentencePiece tokenizer
sp_tokens = sp_tokenizer.tokenize(text)
print(sp_tokens)
```

### Encoding and Decoding

Encode text into token ids and decode back to text. 

**Encoding:** To encode text, use the encode method. 
```python
text = "مثال على النص العربي"  # Example Arabic text

# Using BPE tokenizer
encoded_bpe_output = bpe_tokenizer.encode(text, add_special_tokens=True)
print(encoded_bpe_output)

# Using SentencePiece tokenizer
encoded_sp_output = sp_tokenizer.encode(text, add_special_tokens=True)
print(encoded_sp_output)
```

**Decoding:** To convert token ids back to text, use the decode method:
```python
# Using BPE tokenizer
decoded_bpe_text = bpe_tokenizer.decode(encoded_bpe_output)
print(decoded_bpe_text)

# Using SentencePiece tokenizer
decoded_sp_text = sp_tokenizer.decode(encoded_sp_output)
print(decoded_sp_text)
```

## Available Tokenizers

```bash
Available Tokenizers
get_bpe("bpe32"): Based on BPE Tokenizer with Vocab Size of 32k
get_bpe("bpe50"): Based on BPE Tokenizer with Vocab Size of 50k
get_bpe("bpe64"): Based on BPE Tokenizer with Vocab Size of 64k
get_bpe("bpe86"): Based on BPE Tokenizer with Vocab Size of 86k
get_bpe("bpe32T"): Based on BPE Tokenizer with Vocab Size of 32k (with Tashkeel (diacritics))
get_bpe("bpe50T"): Based on BPE Tokenizer with Vocab Size of 50k (with Tashkeel (diacritics))
get_bpe("bpe64T"): Based on BPE Tokenizer with Vocab Size of 64k (with Tashkeel (diacritics))
get_bpe("bpe86T"): Based on BPE Tokenizer with Vocab Size of 86k (with Tashkeel (diacritics))
get_sp("sp32"): Based on SentencePiece Tokenizer with Vocab Size of 32k
get_sp("sp50"): Based on SentencePiece Tokenizer with Vocab Size of 50k
get_sp("sp64"): Based on SentencePiece Tokenizer with Vocab Size of 64k
get_sp("sp86"): Based on SentencePiece Tokenizer with Vocab Size of 86k
get_sp("sp32T"): Based on SentencePiece Tokenizer with Vocab Size of 32k (with Tashkeel (diacritics))
get_sp("sp50T"): Based on SentencePiece Tokenizer with Vocab Size of 50k (with Tashkeel (diacritics))
get_sp("sp64T"): Based on SentencePiece Tokenizer with Vocab Size of 64k (with Tashkeel (diacritics))
get_sp("sp86T"): Based on SentencePiece Tokenizer with Vocab Size of 86k (with Tashkeel (diacritics))
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
0.2.3

## Citations:
Coming soon


