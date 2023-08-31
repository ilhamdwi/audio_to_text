import speech_recognition as sr

r = sr.Recognizer()

def conversion(file, lang):
    all=[]
    with sr.AudioFile(file) as source:
        print("fetching file")
        audio_text = r.listen(source)
        try:
            print("Converting audio to text.....")
            text = r.recognize_google(audio_text, language=lang)
            all.append(text)
        except:
            print("Sorry, run again.....")
    print(all)

    if all:
        output_file = "file_text/voice3.txt"
        with open(output_file, "w") as txt_file:
            txt_file.write("\n".join(all))
        print(f"Converted text saved to {output_file}")
    else:
        print("No text to save.")

if __name__ == "__main__":
    conversion("file_voice/voice1.wav", "id" )
