class Word_counter:
    def __init__(self, user_input):
        self.user_input = user_input
    def word_count(self):
        counter  = 1
        for char in self.user_input:
            if char == " ":
                counter += 1
        return counter
    def character_counter(self):
        counter = 0
        for char in self.user_input:
            if char != " ":
                counter +=1
        return counter
    def line_counter(self):
        counter = 1
        for char in self.user_input:
            if char == "\n":
                counter += 1
        return counter







user_input = str(input(""" Enter the text you need to analyze:
                        """))

word_counter = Word_counter(user_input)
word_result = word_counter.word_count()
print(f"The amount of words in the text are {word_result}")
character_result = word_counter.character_counter()
print(f"The amount of characters in the text are {character_result}")
line_result = word_counter.line_counter()
print(f"The amount of lines in the text are {line_result}")
