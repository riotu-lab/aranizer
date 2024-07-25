import pkg_resources
from transformers import PreTrainedTokenizerFast

# Dictionary with paths to tokenizers
dc = {
    "bpe32": "tokenizers/bpe/BPE_tokenizer_32.0K.json",
    "bpe50": "tokenizers/bpe/BPE_tokenizer_50.0K.json",
    "bpe64": "tokenizers/bpe/BPE_tokenizer_64.0K.json",
    "bpe86": "tokenizers/bpe/BPE_tokenizer_86.0K.json",
    "sp32": "tokenizers/sp/SP_tokenizer_32.0K.model",
    "sp50": "tokenizers/sp/SP_tokenizer_50.0K.model",
    "sp64": "tokenizers/sp/SP_tokenizer_64.0K.model",
    "sp86": "tokenizers/sp/SP_tokenizer_86.0K.model",
    "bpe32T": "tokenizers/bpe/TBPE_tokenizer_32.0K.json",
    "bpe50T": "tokenizers/bpe/TBPE_tokenizer_50.0K.json",
    "bpe64T": "tokenizers/bpe/TBPE_tokenizer_64.0K.json",
    "bpe86T": "tokenizers/bpe/TBPE_tokenizer_86.0K.json",
    "sp32T": "tokenizers/sp/TSP_tokenizer_32.0K.json",
    "sp50T": "tokenizers/sp/TSP_tokenizer_50.0K.model",
    "sp64T": "tokenizers/sp/TSP_tokenizer_64.0K.model",
    "sp86T": "tokenizers/sp/TSP_tokenizer_86.0K.model"
}

def get_bpe(name):
    tokenizer_path = pkg_resources.resource_filename(__name__, dc[name])
    tokenizer_fast = PreTrainedTokenizerFast(tokenizer_file=tokenizer_path)
    return tokenizer_fast

def get_sp(name):
    tokenizer_path = pkg_resources.resource_filename(__name__, dc[name])
    tokenizer_fast = PreTrainedTokenizerFast(sp_model_file=tokenizer_path)
    return tokenizer_fast
