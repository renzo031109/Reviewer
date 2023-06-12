word = "Test"
box =[]
print("Guess what is the word:")
while True:
    for i in word:
        if i not in box:
            print("_", end=" ")
        else:
            print(i)
        
        
    
    ans = input("\n\nEnter the letter: ")
    if ans in word.split():
        box.append(ans)
    print(box)



