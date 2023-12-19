from transformers import PreTrainedTokenizerFast

def get_tokenizer():
    """
    Initializes and returns a custom tokenizer for Arabic language processing.

    This function loads a tokenizer from a predefined file and enriches its
    vocabulary with a set of Arabic diacritics as special tokens. The tokenizer
    is based on the PreTrainedTokenizerFast class from the transformers library.

    Returns:
        PreTrainedTokenizerFast: A tokenizer with extended vocabulary to
                                 include Arabic diacritics.
    """
    # Initialize the tokenizer
    tokenizer_fast = PreTrainedTokenizerFast(tokenizer_file="BPE_tokenizer/BPE_tokenizer_64.0K.json")

    # List of Arabic diacritics
    arabic_diacritics = ['َ', 'ً', 'ُ', 'ِ', 'ٍ', 'ْ', 'ّ', 'ٓ', '٭', 'ء']

    # Add Arabic diacritics to the tokenizer's vocabulary as special tokens
    num_added_toks = tokenizer_fast.add_tokens(arabic_diacritics, special_tokens=True)

    return tokenizer_fast
