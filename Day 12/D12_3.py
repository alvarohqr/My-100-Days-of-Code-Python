#Global Scope
enemies = "Zombie"

def increase_enemies():
    #the global identifier allows to modify a global variable inside a function
    global enemies 
    enemies  = "Werewolf"
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")
    