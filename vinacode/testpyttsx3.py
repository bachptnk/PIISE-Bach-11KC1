import pyttsx3

PTNK_AI_assistant=pyttsx3.init()  # My name is Bach. I am learning in grade 10 in HIGH SCHOOL FOR THE GIFTED (PTNK)
voice=PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
Brate = 177
PTNK_AI_assistant.setProperty('rate',Brate)
def speak(audio):
    print('PTNK_AI_assistant: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()

speak('xin chào')