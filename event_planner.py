# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
system = "audio sytem + projector" if attendees > 100 else "boom box"
print(venue)
print(system)

food = input("Would you like vegetarian food (yes,no)? ") 
if food == "yes":
    print("Veggie Delight Caterers") 
else:
    print("Gourmet Meals Caterers")

# Task 2: Venue Selection
# Task 3: Catering Choices