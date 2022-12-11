############### Scope ###############

enemies = 1 #global variable

def increase_enemies():
    enemies  = 2 #is local to this function
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")