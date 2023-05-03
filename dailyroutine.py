#daily routine
Name=input("Enter your good name\n")
print(f"Hi {Name}. Good morning.")
choice=input("Are you going to campus today? If yes then type 'y' else type 'n'\n").lower()
def choice():
   
   if choice=='y':
      a=input("Are you going with bike🚲 or with foot👣? if with bike then type 'bike' else type 'walk'\n")
      if a=='bike':
         h=input("Have you worn helmet🪖? if yes then type'y' or type 'no'\n")
         if h=='y':
            c=input("Okay great!😍")
         elif a=='walk':
            print("Okay. Please check proporely while crossing the road🛣️")
      else:
         print("Please wear helmet.🙏") 
   elif choice=='n':
      print("Okay study🏫 hard at home.🏠")

    
   


