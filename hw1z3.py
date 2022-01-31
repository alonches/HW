postcards = {
    "Maria":"London",
    "Lorenzo":"Milan",
    "Oleg":"Canberra",
    "Hans":"Calgary",
    "Mark":"Milan",
    "Alex":"Krakow",
    "Julia":"Murmansk"
}
new_cards = {"Petra":"Paris","Ivan":"Moscow"}
postcards.update(new_cards)
postcards["Oleg"] = "Sydney"

print(len(postcards.values()), "unique cities\n",postcards.values())