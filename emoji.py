def emoji_converter(message):
    words=message.split(' ') #space mukine lakhela words ne alag string j samajshe
    print(words)
    emoji={
         ":)":  "😀",
         ":(": "😒"
    }
    output=""
    for word in words:
         output +=emoji.get(word,word) + " " #second word is defult value
    return output

message=input(">")
result=emoji_converter(message)
print(result)