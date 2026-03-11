from transformers import pipeline

# Load the pipeline with the Whisper model
asr = pipeline("automatic-speech-recognition",
                 model="openai/whisper-base")

# Path to your audio file (.wav or .mp3)
audio_path = "./pipelines/mlk_clip.mp3"   

# Transcribe the audio
result = asr(audio_path, 
             return_timestamps = True, 
             generate_kwargs={"language": "en"})

# Print the transcription
#print("Transcription:", result["text"] )

context = result["text"]
summarize = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarize(f"Summarize the following in 3 sentences:\n{context}")  
print(summary)

