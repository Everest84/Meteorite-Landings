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
    return df

# Ask user for lat, long, radius
def userInput():
    while True:
        coordinates = input("Enter the coordinates separated by a comma.\nLatitude range: -90 to 90 | Longitude range: -180 to 180\n>> ")
        coordinates = coordinates.replace(" ", "")
        latlong = coordinates.split(',')
        latlong_list = list(latlong)
        try:
            lat = float(latlong_list[0])
            long = float(latlong_list[1])
        except ValueError:
            print("Enter a number.\n")
            continue
        else:
            break
    search_radius = float(input("How many kilometers radius?: "))
    return lat, long, search_radius

# Calculate the search area
def searchArea(lat,long,search_radius):
    latitude = math.radians(lat)
    longitude = math.radians(long)
    print(latitude,longitude)

def main():
    getFile()
    lat, long, search_radius = userInput()
    searchArea(lat, long, search_radius)

main()
