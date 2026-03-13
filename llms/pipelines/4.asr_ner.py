from transformers import pipeline
from transformers import logging

logging.set_verbosity_error()

# Load the pipeline with the Whisper model
asr = pipeline("automatic-speech-recognition",  model="openai/whisper-base")

# Path to your audio file (.wav or .mp3)
audio_path = "./pipelines/mlk_speech.mp3"

# Transcribe the audio
result = asr(audio_path, return_timestamps=True,
             generate_kwargs={"language": "en"})

# Print the transcription
# print("Transcription:", result["text"] )

context = result["text"]

ner = pipeline("ner", model="dslim/bert-base-NER")

entities = ner(context)

# Display results
print("\nEntities\n")
for entity in entities:
    print(f"{entity['word']} - ({entity['score']:.2f})")
