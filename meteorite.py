## Program 4.py
## Program 4
## Brian Hare
## CS 101
## Matthew Downs

import math

while True:
    while True:
        f = input("What is the file location?: ")
        try:
            inputFile = open(f, 'r', encoding='utf-8')
        except IOError:
            print("No file under that name.")
            continue
        else:
            break

    header = inputFile.readline() # get only the first line (header)
    newFile = open('Meteorite_Zone.txt', 'w', encoding='utf-8') # create an output file to write to
    newFile.write(header) # put header in output file

    # make a list of each line of f
    f_lines = []
    for i in inputFile.readlines(): 
        f_lines.append(i)

    # get user inputs
    while True:
        while True:
            c_count = 0
            print("Latitude and longitude? Ex: 34,21")
            user_latlong = input("Latitude,Longitude: ")
            for i in user_latlong:
                if i == ',':
                    c_count += 1
            if c_count == 0:
                print("Separate your entries with a comma.")
                continue
            elif c_count > 1:
                print("Use only one comma.")
                continue
            else:
                break

        user_latlong = user_latlong.split(',')
        user_lat = user_latlong[0]
        user_long = user_latlong[1]

        try:
            user_lat = float(user_lat)
            user_long = float(user_long)
        except ValueError:
            print("Enter numbers for your latitude and longitude.")
            continue
        else:
            break

        if user_lat < -90 or user_lat > 90:
            print("Latitude should be between -90 and 90 degrees.")
            continue
        if user_long < -180 or user_long > 180:
            print("Longitude should be between -180 and 180 degrees.")
            continue

    while True:
        try:
            user_rad = float(input("Search area (in miles)?: "))
        except ValueError:
            print("Enter a number.")
            continue
        else:
            break

    meteorite_list = []
    map_coord = []
    for i in f_lines:
        target_lat = i[135:149]
        target_long = i[150:164]
        target_lat.replace(" ","")
        target_long.replace(" ","")
        try:
            target_lat = float(target_lat)
            target_long = float(target_long)
            target_coord = [target_lat, target_long]
            deltaLat = target_lat - user_lat
            deltaLong = target_long - user_long
            a = (math.sin(deltaLat/2))**2 + math.cos(user_lat) * math.cos(target_lat) * (math.sin(deltaLong/2))**2
            c = 2 * math.atan2(a**0.5,(1-a)**0.5)
            d = 3961 * c
            if d < user_rad:
                newFile.write(i)
                meteorite_list.append(d) # no function other than to determine the length of the number of matching meteorites
                map_coord.append(target_coord)
            else:
                continue
        except ValueError:
            continue

    print("Check 'Meteorite_Zone.txt' to see matching meteorites.\n")
    newFile.close()

    user_lat = str(user_lat)
    user_long = str(user_long)
    user_lat.replace(" ","")
    user_long.replace(" ","")
    url = "http://maps.google.com/maps/api/staticmap?center="+user_lat+','+user_long+"&size=512x512&maptype=roadmap"
    x = 0
    while x < len(meteorite_list):
        for i in map_coord:
            i[0], i[1] = str(i[0]), str(i[1])
            url += "&markers=color:blue|label:M|"+i[0]+","+i[1]
            x+=1

    print("Below is a list of up to ten meteorites that matched your conditions. Copy and paste the URL into your web browser to visualise it on a map.\n")
    print(url, '\n')

    start_over = input("Try again? (Y/N)")
    if start_over == 'Y' or start_over == 'y':
        continue
    else:
        break
