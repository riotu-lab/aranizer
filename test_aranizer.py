def test_imports():
    try:
        import aranizer
        print("Import successful.")
    except ImportError as e:
        print(f"Import failed: {e}")

def test_tokenizer():
    try:
        from aranizer import get_bpe, get_sp

        # Test BPE tokenizer
        bpe_tokenizer = get_bpe("bpe32")
        sample_text = "هذا نص تجريبي لاختبار وظيفة التوكنيزر."
        bpe_tokens = bpe_tokenizer.tokenize(sample_text)

        print("BPE Tokenization successful.")
        print("Sample Text:", sample_text)
        print("BPE Tokens:", bpe_tokens)

        # Test SP tokenizer
        sp_tokenizer = get_sp("sp32")
        sp_tokens = sp_tokenizer.tokenize(sample_text)

        print("SP Tokenization successful.")
        print("Sample Text:", sample_text)
        print("SP Tokens:", sp_tokens)
        
        # Encoding and decoding
        encoded_output = sp_tokenizer.encode(sample_text, add_special_tokens=True)
        print("Encoded Output:", encoded_output)
        
        decoded_text = sp_tokenizer.decode(encoded_output)
        print("Decoded Text:", decoded_text)
        
    except Exception as e:
        print(f"Tokenizer test failed: {e}")

if __name__ == "__main__":
    test_imports()
    test_tokenizer()
