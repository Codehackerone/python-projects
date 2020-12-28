from geopy.geocoders import ArcGIS

nom = ArcGIS()


def locator(a):
    coor = nom.geocode(a)
    if coor is None:
        return "Your Place Doesnt Exist"
    else:
        la = coor.latitude
        lo = coor.longitude
        return "Coordinates={},\nLatitude={},Longitude={}".format(coor, la, lo)


while True:
    address = input("Enter address:")
    print(locator(address))
    choice = input("Want to Continue? Y if yes and N if no:")
    if choice == "Y":
        continue
    elif choice == "N":
        break
    else:
        print("Couldn't Understand You.")
        break

print("Thanks for using my program")
