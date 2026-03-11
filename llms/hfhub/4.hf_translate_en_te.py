from huggingface_hub import InferenceClient
import keys

model_id = "facebook/mbart-large-50-many-to-many-mmt"   
#model_id = "facebook/facebook/nllb-200-distilled-600M"
client = InferenceClient(model=model_id, 
                         provider="hf-inference", 
                         token= keys.HUGGINGFACE_KEY)

english_text = "Did you play cricket yesterday?"

response = client.translation(english_text, 
                             src_lang="en_XX",   # Source language (English)
                             tgt_lang="te_IN" )  # Target language (Telugu))

print("Telugu:", response.translation_text)