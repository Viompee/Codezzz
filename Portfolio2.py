#The Code:
#Get the input from the user
# Ask Piattos for his coin count
raw_input = input("How many coins do you have, Piattos? ")
#Check if the input is a valid number
# 1. The try / except Structure (Safety Net)
try:
    coins = int(raw_input)
except:
    coins = -1 
#Then run the logic to pick a power-up
# 2. Multi-way Decisions (if / elif / else) [cite: 507, 511]
if coins == -1:
    print("Error: Please enter a numeric value for your coins.")
elif coins >= 100:
    print("Owwww PALDOOOO! You can afford the Super Star!")
elif coins >= 50:
    print("Eyyy! You can afford the Fire Flower! That op asf.")
elif coins >= 20:
    print("Well, You can afford the Super Mushroom! Not that good but gets the job done. Good Luck!!")
elif coins >= 0:
    print("Sorry Piattos, you no no afford any power ups!")
else:
    print("Wait... how do you have negative coins?")
