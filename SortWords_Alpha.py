my_str = "I'm studying Data Science for the next 1 year"

words = [word.lower() for word in my_str.split()]


words.sort()



print("The sorted words are:")
for word in words:
   print(word)