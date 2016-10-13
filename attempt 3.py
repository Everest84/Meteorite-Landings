import math, string

f = open('C:/UMKC/Fall 2016/CS 101/Program 4/Meteorite_Landings.txt', 'r', encoding='utf-8')
lat1 = float(input("lat?: "))
long1 = float(input("lon?: "))
radius = float(input("miles?: "))

reclat = []
reclon = []
for i in f.readlines():
    i.replace(" ","")
    if i == '':
        continue
    reclat.append(i[135:144])
    reclon.append(i[150:159])
# list of all lat and long in the file
latitudes = reclat[1::]
longitudes = reclon[1::]

x = 0
while x < len(latitudes):
    lat2 = float(latitudes[x])
    long2 = float(longitudes[x])

    deltaLat = lat2 - lat1
    deltaLong = long2 - long1
    a = (math.sin(deltaLat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(deltaLong/2))**2
    c = 2 * math.atan2(a**0.5,(1-a)**0.5)
    d = 3961 * c
    print(d, ' ', x)
    x+=1


