print("Welcome to the blind auction project")
print("\n")

dict1={}
bid='yes'
while (bid=='yes'):
   
    dname=input("Enter your name:")
    dbid=int(input("Enter your bid:"))
    dict1[dname]=dbid
    bid=input("\nAre there any other bidders here? if yes type yes. If it's no type no: ")
    print("------------------------------------------------------------------------------------------")
    if bid=='no':
        max_value=max(dict1.values())
        for key in dict1:
            if dict1[key]==max_value:
                print(f"The winner is {key}")            
       
        
            