# single_quote = 'Hello'
# double_quote = "World"
# triple_quote = """Multi-line 
# string"""
# print (single_quote)
# print (double_quote)
# print (triple_quote)

# text = "Python programming"

# print(text [0])   # (first character)
# print (text [-1]) # (last character)
# print (text[0:6]) # (slice 0 to 5)
# print (text[:6])  # (from start to 5)
# print (text[7:])  # (7 to end)

# name = "bob the builder"

# print (len(name))                   # Length
# print (name.strip())                # Remove whitespace
# print (name.upper())                # Uppercase
# print (name.lower())                # Lowercase
# print (name.title())                # Title case
# print  (name.replace("bob","jane"))   # Replace

# name = "John Doe"
# age = 30

# message_1 = f"My name is {name} and I am {age} years old."               # f-strings
# message_2 = "My name is {} and I am {} years old". format(name,age)      #str.format()
# message_3 = "My name is %s and I am %d years old." % (name,age)          # %-formatting 

text_Exercise = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""
word_count = len(text_Exercise.split())
character_count = len(text_Exercise)
character_count_no_spaces = len(text_Exercise.replace(' ',''))
sentence_count = text_Exercise.count('.') + text_Exercise.count("!") + text_Exercise.count("?")
print(f" The text contains {word_count} words,{character_count} characters,{character_count_no_spaces} characters with no spaces and {sentence_count} sentences.")

