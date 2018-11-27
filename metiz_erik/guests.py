guests = ["Sveta", "Tolik", "Valya", "Olya"]
print("I invite u to dinner, " + guests[0] + "!")
print("I invite u to dinner, " + guests[1] + "!")
print("I invite u to dinner, " + guests[2] + "!")
print("I invite u to dinner, " + guests[3] + "!")

guests.remove("Olya")
print(guests)

guests.insert(3, "Sasha")
print(guests)

print("I invite u to dinner, " + guests[0] + "!")
print("I invite u to dinner, " + guests[1] + "!")
print("I invite u to dinner, " + guests[2] + "!")
print("I invite u to dinner, " + guests[3] + "!")

guests.append("Dima")
print(guests)
