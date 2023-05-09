# #love game

Your_name=input("Enter the first person name\n").lower()
partners_name=input("Enter the second person name\n").lower()


common_word=[]
for word in Your_name:
    if word in partners_name and word not in common_word and word!=" ":
        common_word.append(word)

a=len(common_word)
print(a)
common_word_result=int(a)

if common_word_result>2 and common_word_result<4:
    print("Its complicated")
elif common_word_result>=4 and common_word_result<5:
    print("You guys are good together")
elif common_word_result>=5 and common_word_result<6:
    print("Wow You guys are very nice together")
elif common_word_result>=6 and common_word_result<7:
    print("Perfect! just perfect")
elif common_word_result>=7 and common_word_result<8:
    print("Made for each other")
elif common_word_result>=8:
    print("You guys are can live up in any situation\n")