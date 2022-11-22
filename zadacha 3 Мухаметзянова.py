postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}
new_postcards={"Petra": "Paris", "Ivan": "Moscow"}
postcards.update(new_postcards)
print(postcards)
postcards["Oleg"]="Sidney"
print(postcards)
postcards_values=list(postcards.values())
print(postcards_values)
postcards_values=set(postcards_values)
print(postcards_values)
print(len(postcards_values))
print("Количество уникальных городов:", (len(postcards_values)))
print(*postcards_values, sep=", ")
