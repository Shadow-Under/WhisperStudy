
import whisper
import time

def transcribe_audio():
  
    model = whisper.load_model("base")
    
    
    start_time = time.time()
    
   
    try:
       
        result = model.transcribe("audio.mp3")
        
      
        print("Transcribed Text:")
        print(result["text"])
        
       
        execution_time = time.time() - start_time
        print(f"\nExecution time: {execution_time:.2f} seconds")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    transcribe_audio()
