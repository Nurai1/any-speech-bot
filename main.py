import speech_recognition as s_r
import openai
import pyttsx3 as tts

speaker = tts.init()
speaker.setProperty('rate', 150) 
speaker.setProperty('volume', 0.7)
voice_id = "com.apple.speech.synthesis.voice.karen"
speaker.setProperty('voice', voice_id)

openai.organization = "org-YCorj8O4Him2Mr5BLMVrldM1"
openai.api_key = "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"
openai.Model.list()

r = s_r.Recognizer()

my_mic = s_r.Microphone(device_index=0)

messages = [
    {"role": "system", "content": "You are a helpful assistant who help with English speaking. You can correct me if i use incorrect structure in the sentence. Then answer as an usual Chat Assistant. "}
]

while my_mic:
    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        user_speech = r.recognize_google(audio)
    except:
        speaker.say("Error occured while processing your voice, please say again.")
        speaker.runAndWait()
        continue



    messages.append({ "role": "assistant", "content": user_speech })

    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0,
    )

    botResponseText = response.choices[0].message.content
    messages.append({ "role": "assistant", "content": botResponseText })

    print(botResponseText)

    speaker.say(botResponseText)
    speaker.runAndWait()

