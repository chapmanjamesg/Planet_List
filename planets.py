planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Neptune", "Uranus"])

planet_list.insert(2, "Venus")
planet_list.insert(3, "Earth")

planet_list.append("Pluto")

del planet_list[8]
print(planet_list)