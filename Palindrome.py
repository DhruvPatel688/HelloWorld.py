reverse_answer = []

def word(answer):
    index = -1
    for index in range(len(answer)):
        reverse_answer.append(answer[index])
        index -= 1
    if reverse_answer == answer:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome")



answer  = input("What word would you like to check? ")
word(answer)
