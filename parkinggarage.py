class ParkingGarage:
    def __init__(self):
        self.availableTicket = [1,1,1,1,1,1,1,1,1,1]
        self.parkingSpaces = [1,1,1,1,1,1,1,1,1,1]
        self.currentTicket = {
            "paid" : False
        }

    def kiosk(self):
        self.park = input("\nWelcome to our parking garage! \nOur fee is $20 for the day... \nWhat would you like to do? Park/Pay/Leave \n")
        self.park = self.park.strip().lower()
        if self.park == "park":
            garage.takeTicket()
        elif self.park == "pay":
            garage.payForParking()
        elif self.park == "leave":
            garage.leaveGarage()
        else:
            print("\nDid not receive a valid response.")
            garage.kiosk()


    # Decrease available tickets and Parking spaces by one 
    def takeTicket(self):
        print("\nNew ticket has been taken!")
        self.availableTicket.pop()
        self.parkingSpaces.pop()

        self.availableTicketLength = len(self.availableTicket)
        self.parkingSpacesLength = len(self.parkingSpaces)
        print("\nAvailable tickets: " + str(self.availableTicketLength) + " \nAvailable spaces: " + str(self.parkingSpacesLength))
        garage.kiosk()

    def payForParking(self):
        self.payment = input("\nReady to pay $20? Insert/Back ")
        

        # Check if payment variable is not empty
        if self.payment == "insert":
            print("\nYour ticket has been paid and you have 15 minutes to leave")
            self.payment = True
            self.currentTicket["paid"] = True
            print(self.currentTicket)
        elif self.payment == "back":
            garage.kiosk()
        else:
            print("\nDid not receive a valid response.")
            garage.payForParking()

    def leaveGarage(self):
        if bool(self.currentTicket["paid"]) == True:
            print("\nThank you, have a nice day!")

            self.parkingSpaces.append(1)
            self.availableTicket.append(1)

            self.availableTicketLength = len(self.availableTicket)
            self.parkingSpacesLength = len(self.parkingSpaces)

            print("\nAvailable tickets: " + str(self.availableTicketLength) + " \nAvailable spaces: " + str(self.parkingSpacesLength))
        else:
            print("\nYou must make a payment first...")
            garage.payForParking()
garage = ParkingGarage()
garage.kiosk()