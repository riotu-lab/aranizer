import os
from transformers import PreTrainedTokenizerFast

def load_sentencepiece_tokenizer(model_path):
    return PreTrainedTokenizerFast(tokenizer_file=model_path)

def test_sentencepiece_tokenizer():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "aranizer/tokenizers/sp/SP_tokenizer_32.0K.json")  # Use .json
        tokenizer = load_sentencepiece_tokenizer(model_path)
        
        sample_text = "هذا نص تجريبي لاختبار وظيفة التوكنيزر."
        tokens = tokenizer.tokenize(sample_text)
        
        print("SentencePiece Tokenization successful.")
        print("Sample Text:", sample_text)
        print("Tokens:", tokens)
        
        encoded_output = tokenizer.encode(sample_text, add_special_tokens=True)
        print("Encoded Output:", encoded_output)
        
        decoded_text = tokenizer.decode(encoded_output)
        print("Decoded Text:", decoded_text)
        
    except Exception as e:
        print(f"SentencePiece Tokenizer test failed: {e}")

if __name__ == "__main__":
    test_sentencepiece_tokenizer()
