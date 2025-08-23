
# emoji = {"happy:":"😊",
#         "sad":"😢",
#         "angry":"😠"}
# emotion=input("I am feeling")
# if emotion == "happy":
#     print("i am feeling", emoji["happy"])
# elif emotion == "sad":
#     print("i am feeling", emoji["sad"])
# elif emotion == "angry":
#     print("i am feeling", emoji["angry"])
# else:
#     print("i am not feeling anything")

emoji = {"happy":"😊", "sad":"😢", "angry":"😠"}

emotion = input("I am feeling: ")

if emotion in emoji:
    print("I am feeling", emoji[emotion])
else:
    print("Sorry, I don't know that emotion.")

  
# if emotion == "happy":
#     message.append(f"i am feeling {emoji['happy:']}")
# elif emotion == "sad":
#     message.append(f"i am feeling {emoji['sad']}")
# elif emotion == "angry":
#     message.append(f"i am feeling {emoji['angry']}")
# else:
#     message.append("i am not feeling anything")




    

