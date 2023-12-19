# AraNizer

## Description
AraNizer contains custom tokenizers specifically designed for Arabic language processing. Built with SentencePiece and Byte Pair Encoding (BPE) methodologies, these tokenizers are engineered to be compatible with the `transformers` and `sentence_transformers` libraries. Each tokenizer in the AraNizer collection is optimized for different NLP tasks, accommodating a diverse range of vocabulary sizes to suit various linguistic scenarios.

## Installation
Install AraNizer effortlessly with pip:
```bash
pip install aranizer

Usage 
Start by importing the desired tokenizer from AraNizer:
# Other aranizers: aranizer_bpe50k, aranizer_bpe64k, aranizer_bpe86k, aranizer_sp32k, aranizer_sp50k, aranizer_sp64k, aranizer_sp86k

from aranizer import aranizer_sp32k

Load your tokenizer:

tokenizer = aranizer_sp32k.get_tokenizer()  # Replace aranizer_bpe32k with your chosen tokenizer

Example of tokenizing a text:

text = "مثال على النص العربي"  # Example Arabic text
tokens = tokenizer.tokenize(text)
print(tokens)
```

Encoding Text:
To encode text, use the encode method. This converts a text string into a sequence of token ids:
```bash
text = "مثال على النص العربي"  # Example Arabic text
encoded_output = tokenizer.encode(text, add_special_tokens=True)
print(encoded_output)
```
Decoding Text:
To convert token ids back to text, use the decode method:
```bash
decoded_text = tokenizer.decode(encoded_output)
print(decoded_text)
```

## AraNizers
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
## Requirements:
- transformers
  
## Contact:
For queries or assistance, please contact onajar@psu.edu.sa.

## Acknowledgments:
Special thanks to Prince Sultan University and Riotu Lab, under the guidance of Dr. Lahouari Ghouti and Dr. Anis Koubaa, for their invaluable support.

## Version:
0.1.8

## Citations:
If AraNizer benefits your research, please cite us:
```bash
@misc{AraNizer_2023,
  title={Aranizer: A Custom Tokenizer for Enhanced Arabic Language Processing},
  author={Najar, Omar and Sibaee, Serry and Ghouti, Lahouari and Koubaa, Anis},
  affiliation={Prince Sultan University, Riyadh, Saudi Arabia},
  year={2023},
  howpublished={\url{https://github.com/omarnj-lab/aranizer}}
```


