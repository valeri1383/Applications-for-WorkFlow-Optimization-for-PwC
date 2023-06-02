import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")
text = 'Welcome world'
speaker.Speak(text)
