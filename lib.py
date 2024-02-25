from os import system
option = 0
running=True
destinations = []
price = []
totalPrice = 0
seats = 0


def readPrice():
    global price
    file = open("data/price.txt","r")
    lines = file.readlines()
    for line in lines:
       price.append(float(line))
    file.close()

def writedPrice():
    global price
    price = input("enter the price for new direction: ")
    file = open("data/price.txt","a")
    file.write(f"\n{price}")    
    file.close()



def readDestinations():
    global destinations
    file = open("data/destinations.txt", "r")
    lines = file.readlines()
    
    for line in lines:
        destinations.append(line.strip("\n"))
    file.close()



def renderMenu():
    global option
    system('cls')
    print('OPTION')
    print('1. Search destination')
    print('2. Show destination price for person')
    print('3. Show price for a trip')
    print('4. Write nea price')
    
    print('0. EXIT')
    option = int(input('choose >>> '))





def renderDestinations():
    global totalPrice    
    for i in range(len(destinations)):
        print(f"{i}{destinations[i]:>20}{price[i]:10.2f}")
    input("hit enter to continue...") 
        
def renderPrice():
    system('cls')
    global c
    global totalPrice
    for i in range(len(destinations)):
        print(f"{i}{destinations[i]:>20}{price[i]:10.2f}")
    c =int(input(f"select diretion 0 ....{i}: "))
    seats = int(input("Enter number of tikets: "))
    for i in range(len(destinations)):
        if i == c:
            totalPrice = price[i] * seats
            print(totalPrice)

            yes_no = input("Enter 'Yes' if you agree to pay and 'No' if not: ")
            if yes_no == "Yes":
                print(f"Now you have to pay {totalPrice}")
                input("Hit enter to continue...") 
                
            else:
                seats = 0
                totalPrice = 0
                print("You caceled your trip")
                input("Hit enter to continue...") 
                exit
       
            

def searchDestination():
    destination = input("enter destination name: ")
    found = destination in destinations
    if found:
        print(f"Destination '{destination}' is available ")
       # hw3 continue the idea:
        # ask for ticket quantity
        # calculate total cost : 3 x tickets to....
        #ask for cnfirmation
    else:
        print(f"Destination '{destination}' is unavailable")
    input("enter...")

def chooseDestination():
    system('cls')
    print('Choose your destination')
    print()
