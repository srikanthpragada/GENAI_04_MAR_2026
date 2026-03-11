from transformers import pipeline

classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli")
output = classifier("Apple Released a new iPhone - iPhone 17 Pro",
    candidate_labels = ["education", "politics", "business"],
)
print(output)