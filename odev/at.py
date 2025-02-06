import random
import time
horses=[0,0,0,0,0,0]
choice=int(input("choose a num between 1-6"))
print(f"the hores you picked is Horse {choice}")

finishLine=30
while max(horses) < finishLine:
    for i in range(1,6):
        horses[i]+=random.randint(1,6)
print(horses)
time.sleep(1)
print("competition is over") 
arrangment=sorted(enumerate(horses,start=1), key=lambda x: x[1], reverse=True)   
print("\nResults:")  
for i, (horseNo,distance) in enumerate(arrangment,start=1):
  print(f"{i}. Horse{horseNo} ({distance}) br")
