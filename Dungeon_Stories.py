print ("------------------------------------------")
print("        ,     \    /      ,       ") 
print("       / \    )\__/(     / \      ") 
print("      /   \  (_\  /_)   /   \     ")
print(" ____/_____\__\@  @/___/_____\____") 
print("|             |\../|              |")
print("|              \VV/               |")
print("|   Welcome to Dungeon Stories    |")
print("|_________________________________|")
print(" |    /\ /      \ \       \ /\    | ") 
print(" |  /   V        ) )       V   \  |") 
print(" |/     `       / /        '     \|") 
print(" `              VV                '")
print ("------------------------------------------")
print("")
name= input("Please enter your character name: ")
print ("")
print("⠀⠀⠀⠀⠀⢀⠤⠒")
print("⠀⠤⠤⠄⠊⠁⠀⡜")
print("⠀⠓⡢⣤⣀⡀⠘⢅")
print("⠀⡺⢷⣿⠼⠿⠦⢢")
print("⢠⣉⠀⠤⡎⠉⠀⢱")
print("⠀⠚⢠⠒⢣⠀⠀⡎")
print("⠀⠦⠤⠭⠤⠕⠢⠬")
print ("Hi "+ name +", I'm Hoenheim the master through this Dungeon")
print ("")
print ("I hope you can survive like the other party before you")
print ("you are in a forest also with a bag of tools according to your profession")
def menu():    
    print ("")
    print("1. Fighter")
    print("2. Wizard")
    print("3. Rogue")
    print("4. Ranger")
    print("5. Paladin")
    print ("")
menu()
classe= input ("What is your profession? ")
print ("")
if classe == "1":
    print("Cool, the fighters always have advantage with dexterity and most of them are strong.")
elif classe == "2":
    print("Mmmmm, we can be wizards but very difficult if you are not good enough casting spells.")
elif classe == "3":
    print("Wow, thieves are very hard to find because most of them hide in the shadows.")    
elif classe == "4":
    print("I definetly admire how precise rangers are with the vision and senses in general.")
elif classe == "5":
    print("I'm pretty sure that paladins always have the help of God, I hear about one paladin who escape from this dungeon")
else :
    print("Sorry I didn't notice what you tell me, could you repeat?")
    menu()
    classe= input ("What is your profession? ")
     
