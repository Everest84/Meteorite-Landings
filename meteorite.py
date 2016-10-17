## metorite.py
## Matthew Downs
## CS101
## Brian Hare

### FUNCTIONS TO MAKE

#1. ASK USER FOR FILE INPUT; GET FILE
#2. ASK USER FOR COORDINATES AND SEARCH RADIUS
#3. USING COORD. AND RADIUS, SEARCH THROUGH FILE FOR METEORITES IN THE RADIUS
#4. WRITE A NEW FILE WITH A LIST OF ALL THE METEORITES THAT MATCH USER'S CRITERIA

import math, string

# Getting the input file
def getFile():
    while True:
        try:
            f = input("What is the file name?: ")
            df = open(f, "r", encoding='utf-8')
            print(df)
        except IOError:
            print("No file found under that name.")
            continue
        else:
            break

# Ask user for lat, long, radius
def userInput():
    while True:
        coordinates = input("Enter the coordinates separated by a comma.\nLatitude range: -90 to 90 | Longitude range: -180 to 180\n>> ")
        coordinates = coordinates.replace(" ", "")
        latlong = coordinates.split(',')
        latlong_list = list(latlong)
        try:
            lat1 = float(latlong_list[0])
            long1 = float(latlong_list[1])
        except ValueError:
            print("Enter a number.\n")
            continue
        else:
            break
    search_radius = float(input("How many kilometers radius?: "))
    return lat1, long1, search_radius

# Calculate the search area
def calculate(user_lat, user_long, user_search):
    user_lat, user_long, user_search = lat1, long1, search_radius
    

def main():
    #getFile()
    lat1, long1, search_radius = userInput()
    searchArea(lat1, long1, search_radius)

main()
