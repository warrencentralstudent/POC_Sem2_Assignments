text = input("Enter some text: ")

location = text.find("the")

if location == -1:
    print("The word the is not in the string.")
else:
    print ("The word the is in the string.")
    print("The word the appears at", location)