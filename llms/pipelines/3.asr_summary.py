from transformers import pipeline

# Load the pipeline with the Whisper model
asr = pipeline("automatic-speech-recognition",
               model="openai/whisper-base.en")

# Path to your audio file (.wav or .mp3)
audio_path = "./pipelines/mlk_speech.mp3"   

# Transcribe the audio
result = asr(audio_path, 
             return_timestamps = True
             )

# Print the transcription
#print("Transcription:", result["text"] )

context = result["text"]

# Summarise that speech 
summarize = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarize(f"Summarize the following in 3 sentences:\n{context}")  
print(summary)

