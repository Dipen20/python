#love game

Your_name=input("Enter the first person name\n").lower()
partners_name=input("Enter the second person name\n").lower()

#store each common word in variable common_word 
common_word=[]
for word in Your_name:
    if word in partners_name and word not in common_word and word!=" ":
        common_word.append(word)
#length of tht common word
a=len(common_word)

common_word_result=int(a)


if 2 < common_word_result < 4:
    print("Hmm, it's complicated. Maybe you need more time to get to know each other.🥺")
elif 4 <= common_word_result < 5:
    print("You guys are good together! Keep nurturing your relationship.🤩")
elif 5 <= common_word_result < 6:
    print("Wow! You guys are very compatible. You make a great pair.🥰")
elif 6 <= common_word_result < 7:
    print("Perfect! Just perfect. You two are meant to be together.💖")
elif 7 <= common_word_result < 8:
    print("Made for each other. You have a special connection.😘")
elif common_word_result >= 8:
    print("You guys can thrive in any situation. Your relationship is rock solid!💖💋")

elif common_word_result<2:
    print("Unfortunately, if you are in a relationship, it's better to break up as soon as possible. There's just not enough common ground between you.")  
