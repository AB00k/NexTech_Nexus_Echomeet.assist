from Audio import *
from Transcribe import *
from Agent_implementation import *

recorder = AudioRecorder()

while True:
    print("\n1.Press Enter to Start Recording\2. Exit")
    choice = input("Enter your choice: ")
    if choice == '':
      recorder.start_recording()
      text = transcribe_audio()
      print(f"User: {text}")

      if text.lower() == 'exit':
        exit = 'Good Bye'
        play_audio(exit)
        break
          
      response = agent.run(text)
      print(f"Agent: {response}")
      play_audio(response)
    else:
      break
