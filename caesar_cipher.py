#Program Of Caesar Cipher

#------------------What to do---------------------

''' Step 1: Ask user to enter a word which will be your original word
    Step 2: Ask user to choose either the options: encrypt or decrypt
    Step 3: If User chooses encrypt ask him a shift number and shift the original word
    Step: If user chooses decrypt then original word should be displayed 
'''

def encrypt():
    new_word=""
    for letter in word:
        shift_pos=alphabets.index(letter)+shift_no
        shift_pos%=len(alphabets)
        new_word+=alphabets[shift_pos] 
    print(f"Your encoded word is:{new_word}")     
    
def decrypt():
    new_word=""
    for letter in word:
        shift_pos=alphabets.index(letter)-shift_no
        shift_pos%=len(alphabets)
        new_word+=alphabets[shift_pos] 
    print(f"Your decoded word is:{new_word}")  
    


choice='Y'

while choice=='Y' or choice=='y':
    alphabets=['a','b','c','d','e','f','g','h','i''j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word = input("Enter a word: ").strip().lower()
    option=input("Choose:'Encrypt' OR 'Decrypt':").strip().lower()
    shift_no=int(input("Enter a shift number:"))
    if option=='encrypt':
        encrypt()
    else:
        decrypt()
    
    choice=input("Do you want to continue? (Y/N):").strip().lower()
