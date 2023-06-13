word = "Test"
box =[]
print("Guess what is the word:")
while True:
    for letter in word:
        if letter.lower() not in box:
            print("_", end=" ")
        else:
            print(letter, end=" ")
        
        
    
    ans = input("\n\nEnter the letter: ")

    box.append(ans.lower())
 



