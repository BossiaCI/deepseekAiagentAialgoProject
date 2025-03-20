# String manipulation in python
# split()
sentence = "Python is fun"
words = sentence.split()
print(words)


sentence2 = "Python, is, fun"
words2 = sentence2.split(",")
print(words2)


# join()
new_sentence = "".join(words)
print(new_sentence)


# replace()
text = "I love Java"
updated_text = text.replace("Java","Python")
print(updated_text)


# strip()
message = "     Hello, world    end of it"
print(message)

cleaned_text = message.strip()
print(cleaned_text)
