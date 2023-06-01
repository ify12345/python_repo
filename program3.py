# .......................prompt the user for a phone number....................
city_phone_number  = input("Enter your phone number")


# ........................checkFormat function will return a True or False..............
def checkFormat(city_phone_number):

    if (len(city_phone_number) == 14 and city_phone_number[0] == "(" and city_phone_number[4] == ")" 
        and city_phone_number[5] == " " and city_phone_number[9] == "-"):
        
        numbers = city_phone_number[1:4] + city_phone_number[6:9] + city_phone_number[10:14]
        
        if all(char.isdigit() for char in numbers):
            return True
        else:
            return False
    else:
        return False
    


# ........................verifyAreaCode function will return a True or False..............

def verifyAreaCode(city_phone_number):
    cityList =[["Hamilton", 905],["Ottawa", 613],["Montreal", 514], ["Halifax", 782]]
    city = []

    for citycode in cityList:
        city.append('(' + str(citycode[1]) + ')')
    if city_phone_number[0:5] in city:
         return True
    else:
        return False

# ...................the main body of the program verifying if the function is true or false......
if checkFormat(city_phone_number):
    print("Format OK")
    if verifyAreaCode(city_phone_number) :
        print("Valid Area Code")
    else:
        print("Invalid Area Code")
else:
    print("Format ERROR")