import random
a_z = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o','p','a','s', 'd', 'f', 'g', 'h', 'j', 'k','l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '@', '#', '$', '%', '*', '&']

print("This is a random password generator")
index = 8
password = []
while index > 0:
    p = random.choice(a_z)
    password.append(p)
    index -= 1
print(''.join(password))


