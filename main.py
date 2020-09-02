#Airline Booking Service

#**Create a reservation system which books airline seats. It charges various rates for particular sections of the plane. Example, first class is going to cost more than coach. Keep track of when rooms will be available and can be scheduled.

#Seats function. Hold all the seats of plane in a dictionary where the key is the seat and the value is a boolean for a booked seat.
#Consider adding a function that randomly fills in seats to simulate normal booking conditions

import sys
import random


#Globals. Replace later with a class call
seating_dict = {}

def seating_func():
    columns = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    rows = ("31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44")

    global seating_dict

    invalid_seats = ["D31", "E31", "F31", "G31"]

    
    for row in rows:
        for column in columns:
            temp_entry = f"{column}{row}"
            rand = random.randint(0,10)
            if (temp_entry in invalid_seats):
                seating_dict[temp_entry] = False
            else:
                if rand < 3:
                    seating_dict[temp_entry] = False
                else:
                    seating_dict[temp_entry] = True


def price_func(plane_seat):
    """Takes in plane_seat and returns price"""
    if plane_seat[1:] == "31":
        return "$2,499"
    elif plane_seat[1:] < "37":
        return "$1,499"
    elif plane_seat[1:] < "45":
        return "$999"
    else:
        print("\nError parsing seat price.")

def print_seats():
    """Takes in seating_dict dictionary and outputs available seats into Console in image like format"""
    global seating_dict
    print("\n**Seating Chart**\n", "========"*4, "\n")
    #print by rows ex: Row 31 is first
    i = 1
    output_row = ""
    for seat in seating_dict.keys():
        if i < 10:
            output_row += f"{seat} "
            i += 1
        else:
            output_row += f"{seat}\n"
            print(output_row)
            output_row = ""
            i = 1

def avail_seat(plane_seat):
    """Takes user input seat and checks for availability"""
    global seating_dict
    if seating_dict[plane_seat] == True:
        return f"\n{plane_seat} is available!"
    elif seating_dict[plane_seat] == False:
        return f"\n{plane_seat} is not available."
    else:
        return "\nError in seat lookup availability, Please check that you entered a correct seat."

#Create Dictionary of seats
seating_func()

#UI Input Loop
while True:
    print(r"""            ______
            _\ _~-\___
    =  = ==(____BBA___D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D)""")
    print("\nWelcome to Budget Bus Airlines registration terminal. Please select from the following options.")
    print("\nEnter 1 for seat booking\nEnter 2 for seating chart\nEnter 3 to exit the terminal")
    bba_input = input("\nPlease enter your selection: ")
    if bba_input == "1":
        while True:
            seat_input = input("\nEnter 1 to look up seat availability\nEnter 2 to check seating diagram\nEnter 3 to exit to main menu: ")
            if seat_input == "1":
                #Consider adding input verification to check that user gives correct format, otherwise will produce error
                while True:
                    check_seat = input("\nPlease enter a seat to check availability. Ex. A31\nEnter Quit at any time to exit to previous menu: ").upper()
                    #Seat Booking function call goes here.
                    try:
                        if check_seat[:2].upper() == "QU":
                            break
                        elif (avail_seat(check_seat)) == f"\n{check_seat} is available!":
                            print(f"\n{check_seat} is available!")
                            seat_book = input(f"\nWould you like to book this seat? it will cost {price_func(check_seat)}, please enter Yes or No: ")
                            if seat_book[0].upper() == "Y":
                                seating_dict[check_seat] = False
                                print(f"\nYour seat:{check_seat} is booked, enjoy your flight!")
                                no_input = input("\nPress any key to exit:")
                                print("\nThanks for using BBA, have a good day!")
                                sys.exit()
                            else:
                                print("\nReturning to previous menu. ")
                                break
                        elif (avail_seat(check_seat.upper())) == f"\n{check_seat} is not available.":
                            print(f"\nSorry, {check_seat} is not available, please try another seat.")
                    except:
                            print("\nIncorrect value, please try again or type quit to exit.")
            elif seat_input == "2":
                print_seats()
            elif seat_input == "3":
                break
            else:
                print("\nInvalid input, please try again.")
        no_input = input("\nPress enter to return to main menu: ")
    elif bba_input == "2":
        print_seats()
    elif bba_input == "3":
        print("\nThanks for using BBA, have a good day!")
        sys.exit()
    else:
        print("\nInvalid input, please try again.")