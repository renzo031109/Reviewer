import random

with open('C:\\Users\\renan.r\\documents\\pythonprogram\\hagman.txt','r') as h:
    words = h.readlines()
    
word = random.choice(words)[:-1]
allowedX = 5
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end= " ")
    print("")
    print("")
    
    guess = input(f"Allowed errors left {allowedX} , next guess : ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowedX -= 1
        if allowedX == 0:
            break    
    done = True
    
    for letter in word:
        if letter.lower() not in guesses:
            done = False
     
print(guesses)

if done:
    print(f"You are correct the word is : {word}")
else:
    print(f"Game over the word is {word}")