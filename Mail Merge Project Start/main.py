#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    invited_names = []
    for name in names: 
            invited_names.append(name)
        
for name in range(len(invited_names)):
        invited_names[name] = invited_names[name].replace("\n", "")

for name in invited_names: 
    # Concatenating names
    with open('Mail Merge Project Start/Output/ReadyToSend/'+"letter_for"+name+'.txt', "w") as letter:
        letter.write(f"Dear {name}\n" 
                     + "You are invited to my birthday this Saturday.\n"
                     + "Hope you can make it!\n"
                     + "Alvaro")
        
        