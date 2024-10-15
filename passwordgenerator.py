import os, string, random
Length=0

def take_input():
    length="hello"
    try:
        length=int(input("Enter the length of the password: "))
        
    except:
        print("Please, enter a number!")
        input("Press enter to continue: ")
        os.system("cls"if os.name=="nt" else "clear")

    if isinstance(length,int):
        global Length
        Length=length
        return 0
         
    take_input()

    

take_input()

components=string.ascii_letters+string.punctuation+string.digits
components=list(components)

random.shuffle(components)
components=''.join(components)

password=random.choices(components,k=Length)
print("The generated password is:","".join(password))