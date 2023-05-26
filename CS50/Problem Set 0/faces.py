emotion = str(input("Input emotion: ")).strip()
if emotion == ":)":
    emotion = emotion.replace(":)", "🙂")
elif emotion == ":(":
    emotion = emotion.replace(":(", "🙁")



print(emotion)