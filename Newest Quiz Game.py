print("Welcome to my quiz game!")
print("Please type your answers in lower case only!")
question=input("Do you want to continue playing? ")
if question=="yes":
    print("Nice choice!")
    print("Please do not use numerics to answer te questions.")
else:
    print("Oops!")
    quit()

score=0
answer=input("1.Which of these is edible, fish or flowers or both? ")
if answer=="both":
    print("Correct!")
    score+=1
elif answer=="fish":
    print("Flowers are also edible by some cultures like in China!")
answer=input("2.How many teeth does a chicken posses? ")
if answer=="none":
    print("Correct!")
    score+=1
else:
    print("A chicken does not possess any teeth.")
answer=input("3.How many adresses does a formal letter contain? ")
if answer=="two":
    print("Correct")
    score+=1
else:
    print("Look up on a wesite...the letter should contain two adresses")
answer=input("4.John's father has three sons.Jaden and julius...Who is the third son? ")
if answer=="John":
    print("Correct!")
    score+=1
else:
    print("The third son should be John!Please use your common sense!")
answer=input("5.What is the origin of dreadlocks? ")
if answer=="egypt":
    print("Correct!")
    score+=1
else:
    print("The origin of dreadlocks is Egypt.This is proved by a research done by\
scientists where the burried mummies were found to have the said hairstyles. ")
answer=input("6.A farmer put five fish in a tank.On the first day he found two fish dead.How many fish did he remain with?  ")
if answer=="none":
    print("Correct!Excellent Thinking!")
    score+=1
else:
    print("Fish cannot survive in a tank...they only survive in water!")
answer=input("7.Who is identified as the father of computers? ")
if answer=="charles babbage":
    print("Correct!")
    score+=1
else:
    print("Charles Babbage")
answer=input("8.Who is the second richest person in the world? ")
if answer=="elon musk":
    print("Correct!")
    score+=1
else:
    print("Elon Musk")
answer=input("9.How old was Abraham when he was circumsiced? ")
if answer=="seventy five":
    print("Correct!")
    score+=1
else:
    print("SEVENTY FIVE")
answer=input("10.Is there a world cup for wrestling? ")
if answer=="yes":
    print("Correct!")
    score+=1
else:
    print("There is a world cup for wrestling...search for FOX WORLD CUP on your search engine.")

print("You got",score,"out of ten!")
print("You got"+ str(float(score/10)*100)+"%")


    
